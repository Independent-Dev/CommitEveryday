# TODO : yimhoon 코드 정렬
# TODO : 쿼리 최적화. relationship 적극 활용
# TODO : db.session.commit, flush, begin_commit, rollback 정리

import base64
# coding=utf-8
import io
import json
import random
import string
import sys
import calendar
from datetime import datetime, timedelta
from flask_babel import gettext
from os import path, makedirs, getcwd
from urllib.request import urlopen, Request

import pandas as pd
import shortuuid
from dateutil.relativedelta import relativedelta
from flask import current_app
from flask import redirect, send_file
from flask import render_template, flash
from flask import request
from flask import url_for
from flask import jsonify
from flask_classful import route
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from sqlalchemy import and_, or_, func, distinct, case
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from wtforms import StringField, PasswordField, IntegerField, \
    DateField, FloatField, ValidationError, BooleanField, \
    TextAreaField, MultipleFileField, FieldList
from wtforms.validators import DataRequired, Email, EqualTo, Length
from xhtml2pdf import pisa
from werkzeug import secure_filename
from io import StringIO

class CarBrandForm(FlaskForm):
    # 차 브랜드 이름
    brand_name = StringField('brand_name', validators=[
        DataRequired(message='브랜드명을 입력해주세요.')])

    # 국가명
    country_id = StringField('country_id', validators=[
        DataRequired(message='국가명을 선택해주세요.')])

    # 브랜드 로고
    logo_image = FileField('logo_image')

    # def validate_brand_name(self, field):
    #     if field.data is not 'aaddff':
    #         raise ValidationError(gettext('브랜드 이름은 aaddff여야만 합니다!!'))

    def brand_name_duplicated(self):
        """브랜드명 중복 검사"""
        if CarBrand.query.filter(CarBrand.name == self.brand_name.data).one_or_none() is not None:
            self.brand_name.errors.append('해당 브랜드는 이미 등록되어 있습니다.')
            return False

        return True

    def brand_name_duplicated_update(self, id):
        """브랜드명 중복 검사"""
        car_brand = CarBrand.query.filter(
            and_(
                CarBrand.id != id,
                CarBrand.name == self.brand_name.data
            )
        ).one_or_none()
        if car_brand is not None:
            self.brand_name.errors.append('해당 이름으로는 수정할 수 없습니다.')
            return False

        return True

    def logo_image_validate(self):
        if not is_null_empty(self.logo_image.data):
            self.logo_image_base, image_ext = path.splitext(self.logo_image.data.filename)
            self.logo_image_ext = image_ext.lstrip('.').lower()

            # 확장자 체크
            if self.logo_image_ext not in app.config['CAR_BRAND_IMAGE_EXTS']:
                self.logo_image.errors.append('브랜드 로고 파일 타입이 올바르지 않습니다.')
                return False
            return True
        return False  # todo 여기가 return false여야 하는 것 아닌가? 여기까지 왔다는 건 파일이 없다는 뜻이니까.


class CarBasicInfoForm(FlaskForm):
    brand_id = IntegerField('brand_id', validators=[DataRequired(message='브랜드명을 입력해주세요.')])

    name = StringField('name', validators=[DataRequired(message='차량명을 입력해주세요.')])

    color = StringField('color', validators=[DataRequired(message='색상을 입력해주세요.')])

    images = MultipleFileField('images')

    passenger_count = IntegerField('passenger_count', validators=[DataRequired(message='탑승인원을 입력해주세요.')])

    category = StringField('category', validators=[DataRequired(message='차종(분류)을 입력해주세요.')])

    power_plant_device = StringField('power_plant_device', validators=[DataRequired(message='동력발생장치를 입력해주세요.')])

    released_at = FieldList(StringField('released_at', validators=[DataRequired(message='차량출시일을 확인해주세요.')]))

    def car_name_duplicated(self):
        """차량명 중복 검사"""
        car = Car.query.filter(
            and_(
                Car.name == self.name.data,
                Car.car_brand_id == self.brand_id.data
            )
        ).one_or_none()
        if car is not None:
            self.name.errors.append('한 브랜드에 복수의 차량을 등록할 수 없습니다.')
            return False
        return True

    def car_image_validate(self):
        car_images = request.files.getlist("images")
        if not is_null_empty(car_images):
            for car_image in car_images:
                self.car_image_base, image_ext = path.splitext(car_image.filename)
                self.car_image_ext = image_ext.lstrip('.').lower()

                # 확장자 체크
                if self.car_image_ext not in app.config['CAR_IMAGE_EXTS']:
                    self.car_image.errors.append('확장자가 부적절한 파일이 있습니다.')
                    return False
            return True


    def car_name_duplicated_update(self, id):
        """차량명 중복 검사"""
        car = Car.query.filter(
            and_(
                Car.name == self.name.data,
                Car.car_brand_id == self.brand_id.data,
                Car.id != id
            )
        ).one_or_none()

        if car is not None:
            self.name.errors.append('해당 이름으로는 수정할 수 없습니다.')
            return False
        return True


class CarMotorForm(FlaskForm):
    # 충전 방식
    fill_method = StringField('fill_method', validators=[
        DataRequired(message='차량명을 입력해주세요.')])
    # 급속충전시간
    boost_charge_time = IntegerField('boost_charge_time', validators=[
        DataRequired(message='급속충전시간을 입력하세요.')])
    # 완속충전시간
    slow_charge_time = IntegerField('slow_charge_time', validators=[
        DataRequired(message='완속충전시간을 입력해주세요.')])


class CarEngineForm(FlaskForm):
    # 자동 변속
    is_automatic = StringField('is_automatic', validators=[
        DataRequired(message='자동변속 사용여부를 입력하세요.')])
    # 엔진 변속
    engine_shift = IntegerField('engine_shift', validators=[
        DataRequired(message='엔진변속을 입력해주세요.')])


class CarConvenienceSafetyForm(FlaskForm):
    # 모바일 연동
    has_mobile_linkage = StringField('has_mobile_linkage')
    # 크루즈 컨트롤
    has_cruise_control = StringField('has_cruise_control')
    # 열선 스티어링 휠
    has_heated_stering_wheel = StringField('has_heated_stering_wheel')
    # 열선 시트
    has_heated_sheet = StringField('has_heated_sheet')
    # 에어백 갯수
    airbag_count = IntegerField('airbag_count')
    # 경사로 밀림방지
    has_slope_safe = StringField('has_slope_safe')
    # 급제동 경보
    has_sudden_breaking_alarm = StringField('has_sudden_breaking_alarm')
    # 후방 감지
    has_rear_sensor = StringField('has_rear_sensor')

@app.register_view
class CpAdminView(CpAdminBaseView):
    route_base = '/'
    decorators = [
        login_required,
        roles_required(*UserType.admin.role(RoleFuncType.cp).role_list)
    ]

    @route('/sign/draw/', methods=['GET', 'POST'])
    def sign_draw(self):
        """서명 생성 및 png 파일로 내려받을 수 있는 페이지"""
        return render_template('cpadmin/sign_draw.html')

    @route('/sign/save/', methods=['GET', 'POST'])
    def sign_save(self):
        """서명 신규 등록(서명을 text파일 형식으로 저장)"""
        file_name_input = request.form.get('file_name_input', 0)  # TIform을 통해 전달된 파일명
        data_url = request.form.get('data_url', 0)  # 전달된 data url 형식의 이미지.

        if not file_name_input:
            return json_response({
                'success': False,
                'message': "파일명이 존재하지 않습니다."
            })
        if not data_url:
            return json_response({
                'success': False,
                'message': "먼저 사인을 하세요"
            })

        try:
            # 파일명에서 확장자를 제외한 부분만 추출한 뒤 그 이름으로 텍스트 파일 만들기
            with open(file_name_input.split(".")[0]+".txt", "w") as f:
                f.write(data_url)
                return json_response({
                    'success': True,
                    'message': file_name_input
                })
        except (FileNotFoundError, IOError) as e:
            print(e)
            return json_response({
                'success': False,
                'message': "파일 저장에 실패했습니다."
            })

    @route('/sign/show/<string:file_name>/', methods=['GET', 'POST'])
    def sign_show(self, file_name):
        """작성한 서명 확인 페이지"""
        # file_name이 존재하지 않으면 예외를 발생시켜 에러 처리를 하는 부분.
        try:
            with open(file_name+".txt", "r") as f:
                src = f.read()
                return render_template('cpadmin/sign_show.html', src=src)
        except (FileNotFoundError, IOError) as e:
            print(e)
            return render_template(
                '/sign_show.html',
                fail="true",
                error="해당 이름의 사인이 없습니다."
            )

    @route('/check/multifile/input/', methods=['GET', 'POST'])
    def check_multi_file_input(self):
        """파일 다중 업로드 UI"""
        return render_template('check/check_multi_file_input.html')

    @route('/check/multifile/action/', methods=['GET', 'POST'])
    def check_multi_file_action(self):
        """파일 다중 업로드 처리"""
        files = request.files.getlist('files')  # 일반 POST 배열은 request.form.getlist('')로 가능.
        file_list = [afile.filename for afile in files]

        return render_template('check/check_multi_file_input.html', file_list=file_list)

    @route('/check/chart_js/', methods=['GET', 'POST'])
    def check_chartJS(self):
        """차트 그리기 체크"""
        color_list = [('red', 300), ('blue', 50), ('yellow', 100), ('pink', 300)]
        return render_template('check/check_chart_js.html', color_list=color_list)

    @route('/check/add/', methods=['GET', 'POST'])
    def check_add(self):
        """옵션 추가/삭제 연습 페이지"""
        return render_template('check/check_add_and_delete.html', current_year=datetime.now().year)

    @route('/check/add/day', methods=['GET', 'POST'])
    def check_add_day(self):
        """차량출시일 날짜 변경 ajax연습"""
        year = request.args.get("year", 1, int)

        month = request.args.get("month", 1, int)

        if not year:
            return json_response({
                'success': False,
                'message': '연도를 입력해주세요'
            })

        if not month:
            return json_response({
                'success': False,
                'message': "달을 입력해주세요"
            })

        _, day = calendar.monthrange(year, month)

        return json_response({
            'success': True,
            'day': day
        })

    @route('/check/scroller/', methods=['GET', 'POST'])
    def check_scroller(self):
        """slick content scroller 연습"""
        return render_template('check/check_content_scroller.html')

    @route('/check/modal/', methods=['GET', 'POST'])
    def check_modal(self):
        """slick content scroller 연습"""
        return render_template('check/check_modal.html')

    @route('/check/magnific/', methods=['GET', 'POST'])
    def check_magnific(self):
        """magnific 연습"""
        car_list = Car.query.filter().all()
        return render_template('check/check_magnific.html', car_list=car_list)

    @route('/check/download/pdf/', methods=['GET', 'POST'])
    def check_download_pdf(self):
        """pdf 다운로드"""
        xhtml = render_template('check/check_pdf_download.html')
        # xhtml = xhtml1.decode('utf-8')
        pdf_io = io.BytesIO()
        pisa.CreatePDF(xhtml.encode('utf-8'), dest=pdf_io)
        pisa.CreatePDF(xhtml.encode('utf-8'), dest=pdf_io, encoding="utf-8")

        pdf_io.seek(0)
        pdf_io.seek(0)
        return send_file(
            pdf_io,
            attachment_filename="안녕하세요.pdf".format(
                datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            ),
            as_attachment=True,
            cache_timeout=0,
            mimetype='application/pdf'
        )

    # for Car Brand
    @route('/car/brand/list/page/', methods=['GET', 'POST'])
    def car_brand_list_page(self):
        """자동차 브랜드 리스트"""
        # 처리 요청 타입
        action_type = request.args.get("action_type")
        # 검색 조건
        search_option = request.args.get("search_option")
        # 검색 키워드
        brand_search_text = request.args.get("brand_search_text")
        # 검색 시작일
        search_start_day = request.args.get("search_start_day")
        # 검색 종료일
        search_end_day = request.args.get("search_end_day")
        # for paging
        perpage = request.args.get('per_page', 10, int)
        page = request.args.get('page', 1, int)

        # 모든 자동차 브랜드 객체
        car_brand_list = CarBrand.query.order_by(CarBrand.id.desc())  # asc, 오름차순이 default.

        """자동차 브랜드 필터링"""
        # 검색 키워드가 있는 경우에 필터링.
        if not is_null_empty(brand_search_text):
            brand_search_text = brand_search_text.strip()
            if search_option:
                if search_option == 'brand_name':
                    car_brand_list = car_brand_list.filter(
                        CarBrand.name.like('%' + brand_search_text + '%')
                    )
                # 국가명(name_ko)은 CarBrand에 없어서 두 테이블을 join.
                elif search_option == 'country_name':
                    car_brand_list = car_brand_list.join(
                        CodeCountry, CarBrand.code_country_id == CodeCountry.id
                    ).filter(
                        CodeCountry.name_ko.like('%' + brand_search_text + '%')
                    )
            else:
                car_brand_list = car_brand_list.join(
                    CodeCountry, CarBrand.code_country_id == CodeCountry.id
                ).filter(
                    or_(CarBrand.name.like('%'+brand_search_text+'%'),
                        CodeCountry.name_ko.like('%' + brand_search_text + '%'))
                )

        # 날짜 검색 옵션
        if search_start_day and search_end_day:
            search_date = SearchDate()
            search_end_day = search_date.get_search_day(search_end_day, end_date=True)
            car_brand_list = car_brand_list.filter(CarBrand.registered_at.between(search_start_day, search_end_day))

        """엑셀 다운로드 로직"""
        if action_type == 'excel_download':
            column_names = (
                "브랜드 번호",
                "브랜드명",
                "국가",
                "로고 이미지",
                "등록일"
            )

            # set comprehension: { key : value for key, value in data }, 아래의 경우에는 { name : [] } 형식.
            data_set = {
                name: [] for name in column_names
            }

            car_brand_list = car_brand_list.all()

            for car_brand in car_brand_list:
                data_set[column_names[0]].append(car_brand.id)  # 브랜드 아이디
                data_set[column_names[1]].append(car_brand.name)  # 브랜드 이름
                data_set[column_names[2]].append(car_brand.code_country.name_ko)  # 국가
                data_set[column_names[3]].append(car_brand.car_brand_image_upload_file.file_url)  # 로고 이미지 출력은 더 생각해보기. 파일이미지를 excel에서 알아먹을 수 있는 방식으로 인코딩하기.
                data_set[column_names[4]].append(car_brand.registered_at.strftime("%Y-%m-%d"))  # noqa: E501

            sheet_name = "BRAND_LIST.{}".format(
                datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            )
            df = pd.DataFrame(data_set)  # pandas의 기본 자료구조. 2차원 배열 또는 리스트, data table 전체를 포함하는 object.
            output = io.BytesIO()  # 바이트 배열을 이진 파일로 다룰 수 있게 해주는 클래스. 이진 파일은 "논-텍스트 파일"을 의미하는 용어로 사용된다.컴퓨터 파일로 컴퓨터 저장과 처리 목적을 위해 이진 형식으로 인코딩된 데이터를 포함한다.
            writer = pd.ExcelWriter(output, engine='xlsxwriter')  # 데이터프레임 오브젝트를 엑셀 시트에 쓰기 위한 클래스. output은 파일이 저장되는 (여기서는 임시) 파일의 위치(이걸 서버에 저장할 것이 아니므로)
            df.to_excel(writer, sheet_name=sheet_name, index=False,
                        columns=column_names)  # writer 자리에는 File path 또는 기존의 엑셀라이터를 쓸 수 있음. index는 row번호. columns은 칼럼명.
            writer.save()

            # construct response
            output.seek(0)  # 탐색 위치를 선두로 되돌림. 엑셀 파일의 데이터가 처음부터 출력될 수 있도록.
            return send_file(  # Sends the contents of a file to the client.
                output,  # 엑셀(보내는 데이터)의 내용을 담은 파일
                attachment_filename="{}.xlsx".format(sheet_name),  # 첨부 파일의 이름.
                as_attachment=False,  # attachment 정보를 담은 header의 송신 여부. False를 하면 파일 이름이 넘어가지 않음. default는 '다운로드'인 것 같다...
                cache_timeout=0,  # 캐시 데이터 유지 시간.
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # noqa: E501 # Multipurpose Internet Mail Extensions의 약자. 파일 변환 방식. HTTP 헤더에 파일이나 자원을 포함하는 바이트 stream 앞에 보냄. (전송방식 더 세밀하게 이해할 것!!)
            )

        return render_template(
                'car/brand/brand_list.html',
                car_brand_list=car_brand_list.paginate(page=page, per_page=perpage,
                                                       error_out=False)
            )

    @route('/car/brand/add/page/', methods=['GET', 'POST'])
    def car_brand_add_page(self):
        """자동차 브랜드 추가 페이지"""
        return render_template('car/brand/brand_add.html')

    @route('/car/brand/add/action/', methods=['GET', 'POST'])
    def car_brand_add_action(self):
        """자동차 브랜드 저장 실행"""
        success = True

        car_brand_form = CarBrandForm()

        car_brand_image = car_brand_form.logo_image.data
        if not car_brand_image:
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['등록할 이미지 선택해주세요.']})
            })

        # 폼 유효성, 브랜드 이름, 로고 확장자 검사
        if False in (car_brand_form.validate_on_submit(),
                     car_brand_form.brand_name_duplicated(),
                     car_brand_form.logo_image_validate()):
            return json_response({
                'success': False,
                'message': json.dumps(car_brand_form.errors)
            })

        try:
            # 데이터베이스에 차량 브랜드 입력
            car_brand = CarBrand(
                name=car_brand_form.brand_name.data,
                code_country_id=car_brand_form.country_id.data,
                code_country=CodeCountry.query.get(car_brand_form.country_id.data),
                registered_at=datetime.utcnow()  # 세계 협정시.
            )

            # 브랜드 로고 이미지 저장 및 데이터베이스에 입력
            logo_image_base, logo_image_ext = path.splitext(car_brand_image.filename)  # 입력받은 경로를 확장자 부분과 그 외의 부분으로 나눔.
            logo_image_ext = logo_image_ext.lstrip('.').lower()  # lstrip의 매개변수는 문자열의 맨 왼쪽 끝에서 제거되어야 할 문자를 지정함. 여기선 .을 제거.

            logo_image = CarBrandImageUploadFile(
                queue_suuid=shortuuid.uuid(),
                file_suuid=shortuuid.uuid(),
                file_base=logo_image_base,
                file_ext=logo_image_ext,
                registered_at=datetime.utcnow()
            )
            car_brand.car_brand_image_upload_file = logo_image

            db.session.add(car_brand)
            db.session.commit()

            logo_image_save_path, _ = path.split(logo_image.file_path)  # file_path를 넘기면 디렉토리 경로, (경로를 제외한)파일명을 전달. 각각 맨 뒤와 맨 앞에 "/" 없음.
            makedirs(logo_image_save_path, exist_ok=True)
            car_brand_image.save(logo_image.file_path)

            # 썸네일과 프리뷰를 만드는 함수
            cp_task.make_preview_thumb(logo_image)

        except Exception as e:
            print(e)
            db.session.rollback()
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['정상적으로 등록되지 않았습니다.']})  # json.dumps: 넘겨준 파이썬 객체를 문자열로 변환
            })

        return json_response({'success': success})

    @route('/car/brand/delete/', methods=['GET', 'POST'])
    def car_brand_delete(self):
        """자동차 브랜드 삭제"""
        id_list = request.form.getlist('brand_id')

        if not id_list:
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['삭제할 브랜드를 선택해주세요.']})
            })

        error_brand = []
        # 삭제하려는 브랜드 가운데 차량이 등록된 것의 id를 error_brand에 append.
        for id in id_list:
            if Car.query.filter(Car.car_brand_id == id).all():
                error_brand.append(id)

        # error_brand에 데이터가 있으면 return.
        if error_brand:
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['{}번 브란드는 차량이 등록되어 있어 삭제할 수 없습니다.'.format(error_brand)]})
            })

        try:
            for id in id_list:
                logo_image = CarBrandImageUploadFile.query.filter_by(car_brand_id=id).one()  # 가독성을 위해 filter_by를 이용함.
                logo_image.delete_file()
                logo_image.delete_thumb()
                logo_image.delete_preview()

                db.session.delete(logo_image)

            CarBrand.query.filter(
                CarBrand.id.in_(id_list)
            ).delete(synchronize_session=False)
            db.session.commit()

        except Exception as e:
            print(e)
            db.session.rollback()
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['삭제가 정상적으로 이루어지지 않았습니다.']})
            })

        return json_response({'success': True})

    @route('/car/brand/update/page/<int:brand_id>/', methods=['GET', 'POST'])
    def car_brand_update_page(self, brand_id):
        """자동차 브랜드 정보 수정 페이지"""
        car_brand = CarBrand.query.get(brand_id)
        return render_template('car/brand/brand_update.html', car_brand=car_brand)

    @route('/car/brand/update/action/<int:brand_id>/', methods=['GET', 'POST'])
    def car_brand_update_action(self, brand_id):
        """자동차 브랜드 정보 수정 실행"""
        success = True
        message = None
        car_brand_form = CarBrandForm()

        # 폼 유효성, 이름 중복, 로고 확장자 검사
        if False in (car_brand_form.validate_on_submit(),
                     car_brand_form.brand_name_duplicated_update(brand_id)):
            return json_response({
                'success': False,
                'message': json.dumps(car_brand_form.errors)
            })

        try:
            car_brand = CarBrand.query.get(brand_id)
            car_brand.name = car_brand_form.brand_name.data
            car_brand.code_country_id = car_brand_form.country_id.data
            car_brand.code_country = CodeCountry.query.get(car_brand_form.country_id.data)

            # 로고 이미지 데이터 수정 로직.
            car_brand_image = car_brand_form.logo_image.data
            if car_brand_image:
                if not car_brand_form.logo_image_validate():
                    return json_response({
                        'success': False,
                        'message': json.dumps(car_brand_form.errors)
                    })
                logo_image_base, logo_image_ext = path.splitext(
                    car_brand_image.filename)
                logo_image_ext = logo_image_ext.lstrip('.').lower()

                logo_image = CarBrandImageUploadFile.query.filter_by(
                    car_brand_id=brand_id
                ).one()
                logo_image.delete_file()
                logo_image.delete_thumb()
                logo_image.delete_preview()

                logo_image.queue_suuid = shortuuid.uuid()
                logo_image.file_suuid = shortuuid.uuid()
                logo_image.file_base = logo_image_base
                logo_image.file_ext = logo_image_ext
                logo_image.car_brand_id = car_brand.id

                car_brand.car_brand_image_upload_file = logo_image
                logo_image_save_path, _ = path.split(logo_image.file_path)
                makedirs(logo_image_save_path, exist_ok=True)
                car_brand_form.logo_image.data.save(logo_image.file_path)
                cp_task.make_preview_thumb(logo_image)

            db.session.add(car_brand)

        except Exception as e:
            print(e)
            db.session.rollback()
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['정상적으로 수정되지 않았습니다.']})
            })

        db.session.commit()

        return json_response({
            'success': success,
            'message': message
        })

    # for Car
    @route('/car/list/page/', methods=['GET', 'POST'])
    def car_list_page(self):
        """자가용 리스트"""
        action_type = request.args.get("action_type")
        # 차량명
        car_name = request.args.get("car_name")
        # 차량 분류
        car_category = request.args.get("car_category_search_option")
        # 동력발생장치
        car_power_plant_device = request.args.get("car_power_plant_device_search_option")
        # 크루즈 컨트롤
        has_cruise_control = request.args.get("has_cruise_control")

        # for paging
        perpage = request.args.get('per_page', 10, int)
        page = request.args.get('page', 1, int)

        # 자동차 객체 리스트
        car_list = Car.query.order_by(Car.id.desc())

        # 차트에 띄우기 위한 브랜드 리스트
        brand_list = db.session.query(
            CarBrand, func.count(CarBrand.id)
        ).join(Car).group_by(CarBrand)

        """자동차와 브랜드 필터링"""
        if car_name:
            car_list = car_list.filter(Car.name.like('%' + car_name + '%'))
            brand_list = brand_list.filter(Car.name.like('%' + car_name + '%'))
        if car_category:
            car_list = car_list.filter(Car.category == car_category)
            brand_list = brand_list.filter(Car.category == car_category)
        if car_power_plant_device:
            car_list = car_list.filter(Car.power_plant_device == car_power_plant_device)
            brand_list = brand_list.filter(Car.power_plant_device == car_power_plant_device)
        if has_cruise_control:
            car_list = car_list.filter(Car.has_cruise_control == has_cruise_control)
            brand_list = brand_list.filter(Car.has_cruise_control == has_cruise_control)

        # 엑셀 다운로드 로직
        if action_type == 'excel_download':
            column_names = (
                "차량 번호",
                "차량명",
                "분류",
                "차량 이미지",
                '동력발생장치',
                '크루즈 컨트롤',
                '에어백 개수'
            )
            data_set = {
                name: [] for name in column_names
            }

            car_list = car_list.all()

            for _, car in enumerate(car_list):
                data_set[column_names[0]].append(car.id)  # 차량 아이디
                data_set[column_names[1]].append(car.name)  # 차량명
                data_set[column_names[2]].append(car.category)  # 차량 분류
                data_set[column_names[3]].append(car.car_image_upload_file[0].preview_url)  # 차량 분류
                data_set[column_names[4]].append(car.power_plant_device.value)  # 동력발생장치
                data_set[column_names[5]].append(car.has_cruise_control.value)  # 크루즈컨트롤
                data_set[column_names[6]].append(car.airbag_count)  # 에어백 개수

            sheet_name = "CAR_LIST.{}".format(
                datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            )
            df = pd.DataFrame(data_set)
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, sheet_name=sheet_name, index=False,
                        columns=column_names)

            writer.save()

            # construct response
            output.seek(0)
            return send_file(
                output,
                attachment_filename="{}.xlsx".format(sheet_name),
                as_attachment=True,
                cache_timeout=0,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                # noqa: E501
            )

        return render_template(
            'car/list.html',
            car_list=car_list.paginate(page, perpage, False),
            brand_list=brand_list.all(),
        )

    @route('/car/add/page/', methods=['GET', 'POST'])
    def car_add_page(self):
        """자가용 추가 페이지"""
        brand_list = CarBrand.query.all()
        return render_template('car/add.html', current_year=datetime.utcnow().year, brand_list=brand_list)  # 출시일을 위해 current_year 데이터를 넘겨줌.

    @route('/car/add/action/', methods=['GET', 'POST'])
    def car_add_action(self):
        """자가용 저장 실행"""
        success = True

        car_basic_info_form = CarBasicInfoForm()

        car_images = car_basic_info_form.images.data
        if not car_images:
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['등록할 이미지를 선택해주세요.']})
            })

        # 폼 유효성, 차 이름 및 브랜드 동시 중복, 이미지 확장자 검사
        if False in (car_basic_info_form.validate_on_submit(),
                     car_basic_info_form.car_name_duplicated(),
                     car_basic_info_form.car_image_validate()):
            return json_response({
                'success': False,
                'message': json.dumps(car_basic_info_form.errors)
            })
        try:
            car_convenience_safety_form = CarConvenienceSafetyForm()
            # 빈 칸을 제거하는 로직.
            option_list = [option for option in request.form.getlist("option") if option]

            # 필수 항목들은 일괄적으로 입력
            car = Car(
                car_brand_id=car_basic_info_form.brand_id.data,
                car_brand=CarBrand.query.get(car_basic_info_form.brand_id.data),
                name=car_basic_info_form.name.data,
                color=car_basic_info_form.color.data,
                passenger_count=car_basic_info_form.passenger_count.data,
                category=car_basic_info_form.category.data,
                released_at="-".join(request.form.getlist("released_at")),
                power_plant_device=car_basic_info_form.power_plant_device.data,
            )

            # 이하 필수가 아닌 항목들은 하나 하나 데이터가 들어있는지 체크한 이후 입력,
            if car_convenience_safety_form.has_mobile_linkage.data:
                car.has_mobile_linkage = car_convenience_safety_form.has_mobile_linkage.data

            if car_convenience_safety_form.has_cruise_control.data:
                car.has_cruise_control = car_convenience_safety_form.has_cruise_control.data

            car.has_heated_stering_wheel = 'Y' if car_convenience_safety_form.has_heated_stering_wheel.data else 'N'  # 이건 체크박스라 이런 식으로 처리함.

            if car_convenience_safety_form.has_heated_sheet.data:
                car.has_heated_sheet = car_convenience_safety_form.has_heated_sheet.data

            car.airbag_count = car_convenience_safety_form.airbag_count.data

            if car_convenience_safety_form.has_slope_safe.data:
                car.has_slope_safe = car_convenience_safety_form.has_slope_safe.data

            if car_convenience_safety_form.has_sudden_breaking_alarm.data:
                car.has_sudden_breaking_alarm = car_convenience_safety_form.has_sudden_breaking_alarm.data

            if car_convenience_safety_form.has_rear_sensor.data:
                car.has_rear_sensor = car_convenience_safety_form.has_rear_sensor.data

            if option_list:
                car.option_list = option_list

            # 차량 이미지 저장, 입력
            for image in car_images:
                car_image_base, car_image_ext = path.splitext(image.filename)
                car_image_ext = car_image_ext.lstrip('.').lower()

                car_image = CarImageUploadFile(
                    queue_suuid=shortuuid.uuid(),
                    file_suuid=shortuuid.uuid(),
                    file_base=car_image_base,
                    file_ext=car_image_ext,
                    registered_at=datetime.utcnow()
                )
                car.car_image_upload_file.append(car_image)

                car_image_save_path, _ = path.split(car_image.file_path)
                makedirs(car_image_save_path, exist_ok=True)
                image.save(car_image.file_path)

                # 프리뷰와 썸네일을 만드는 로직.
                cp_task.make_preview_thumb(car_image)

            # 동력발생장치가 모터인 경우와 모터가 아닌 경우를 나누어서 체크.
            if car_basic_info_form.power_plant_device.data == "MOTOR":
                car_motor_form = CarMotorForm()
                motor = Motor(
                    car_id=car.id,
                    fill_method=car_motor_form.fill_method.data,
                    boost_charge_time=car_motor_form.boost_charge_time.data,
                    slow_charge_time=car_motor_form.slow_charge_time.data
                )
                car.motor = motor

            else:
                car_engine_form = CarEngineForm()
                engine = Engine(
                    car_id=car.id,
                    car=car,
                    engine_shift=car_engine_form.engine_shift.data,
                    is_automatic=car_engine_form.is_automatic.data
                )
                car.engine = engine

            db.session.add(car)
            db.session.commit()

        except Exception as e:
            print(e)
            db.session.rollback()
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['정상적으로 등록되지 않았습니다.']})
            })

        return json_response({'success': success})

    @route('/car/update/page/<int:car_id>/', methods=['GET', 'POST'])
    def car_update_page(self, car_id):
        """자가용 정보 수정 페이지"""
        brand_list = CarBrand.query.all()
        car = Car.query.get(car_id)

        # 수정 페이지에는 해당 출시일과 출시달의 일수 데이터이 미리 들어가 있어야 하므로...
        year, month, _ = [int(x) for x in str(car.released_at).split(" ")[0].split("-")]

        # 출시된 달의 일수
        _, days = calendar.monthrange(year, month)

        return render_template('car/update.html',
                               car=car, brand_list=brand_list, days=days)

    @route('/car/update/action/<int:car_id>/', methods=['GET', 'POST'])
    def car_update_action(self, car_id):
        success = True

        car_basic_info_form = CarBasicInfoForm()
        if False in (car_basic_info_form.validate_on_submit(),
                     car_basic_info_form.car_name_duplicated_update(car_id)):  # 등록시와는 다르게 자신과 아이디가 다른 차량 가운데 차량명과 브랜드가 일치하는 차량이 있을 시 에러.
            return json_response({
                'success': False,
                'message': json.dumps(car_basic_info_form.errors)
            })

        try:
            car = Car.query.get(car_id)

            # 현재 수정하려는 차량의 동력발생장치를 확인하여 삭제. 동력발생장치에 수정이 이뤄지는 경우에만 변경이 되도록 할 수도 있지만, 너무 번거로움.
            if car.power_plant_device.name == "ENGINE":
                db.session.delete(Engine.query.filter(Engine.car_id == car_id).one())
            else:
                db.session.delete(Motor.query.filter(Motor.car_id == car_id).one())

            db.session.commit()

            # 동력 발생장치 객체를 car에 다시 입력.
            if car_basic_info_form.power_plant_device.data == "MOTOR":
                car_motor_form = CarMotorForm()
                motor = Motor(
                    car_id=car.id,
                    fill_method=car_motor_form.fill_method.data,
                    boost_charge_time=car_motor_form.boost_charge_time.data,
                    slow_charge_time=car_motor_form.slow_charge_time.data
                )
                car.motor = motor

            else:
                car_engine_form = CarEngineForm()
                engine = Engine(
                    car_id=car.id,
                    engine_shift=car_engine_form.engine_shift.data,
                    is_automatic=car_engine_form.is_automatic.data
                )
                car.engine = engine

            # car 객체의 필수 정보 수정
            car.car_brand_id = car_basic_info_form.brand_id.data
            car.car_brand = CarBrand.query.get(car_basic_info_form.brand_id.data)
            car.name = car_basic_info_form.name.data
            car.color = car_basic_info_form.color.data
            car.passenger_count = car_basic_info_form.passenger_count.data
            car.category = car_basic_info_form.category.data
            car.released_at = "-".join(request.form.getlist("released_at"))
            car.power_plant_device = car_basic_info_form.power_plant_device.data

            car_convenience_safety_form = CarConvenienceSafetyForm()
            option_list = [option for option in request.form.getlist("option") if option]

            # car 객체에서 필수가 아닌 요소 수정.
            car.has_mobile_linkage = car_convenience_safety_form.has_mobile_linkage.data
            car.has_cruise_control = car_convenience_safety_form.has_cruise_control.data
            car.has_heated_stering_wheel = 'Y' if car_convenience_safety_form.has_heated_stering_wheel.data else 'N'
            car.has_heated_sheet = car_convenience_safety_form.has_heated_sheet.data
            car.airbag_count = car_convenience_safety_form.airbag_count.data
            car.has_slope_safe = car_convenience_safety_form.has_slope_safe.data
            car.has_sudden_breaking_alarm = car_convenience_safety_form.has_sudden_breaking_alarm.data
            car.has_rear_sensor = car_convenience_safety_form.has_rear_sensor.data
            car.option_list = option_list


            car_images = car_basic_info_form.images.data

            # 등록할 이미지가 없는 경우에는 바로 수정.
            if car_images[0]:  # if car_images:를 하면 넘긴 이미지가 없어도 있다고 나오고 len()도 1로 나옴.
                if not car_basic_info_form.car_image_validate():
                    return json_response({
                        'success': False,
                        'message': json.dumps(car_basic_info_form.errors)
                    })

                # 이미지를 추가
                for image in car_images:
                    car_image_base, car_image_ext = path.splitext(image.filename)
                    car_image_ext = car_image_ext.lstrip('.').lower()

                    car_image = CarImageUploadFile(
                        queue_suuid=shortuuid.uuid(),
                        file_suuid=shortuuid.uuid(),
                        file_base=car_image_base,
                        file_ext=car_image_ext,
                        registered_at=datetime.utcnow()
                    )
                    car.car_image_upload_file.append(car_image)



                    car_image_save_path, _ = path.split(car_image.file_path)
                    makedirs(car_image_save_path, exist_ok=True)
                    image.save(car_image.file_path)
                    cp_task.make_preview_thumb(car_image)

            db.session.add(car)
            db.session.commit()

        except Exception as e:
            print(e)
            db.session.rollback()
            return json_response({
                'success': False,
                'message': json.dumps({'add_error': ['정상적으로 수정되지 않았습니다.']})
            })

        return json_response({'success': success})

    @route('/car/download/pdf/<int:car_id>/', methods=['GET', 'POST'])
    def car_download_pdf(self, car_id):
        """pdf 다운로드"""
        car = Car.query.get(car_id)

        released_at = [int(x) for x in str(car.released_at).split(" ")[0].split("-")]
        _, days = calendar.monthrange(released_at[0], released_at[1])
        xhtml = render_template('car/pdf_download.html',
                                car=car, released_at=released_at)
        pdf_io = io.BytesIO()
        pisa.CreatePDF(xhtml.encode('utf-8'), dest=pdf_io)
        pisa.CreatePDF(xhtml.encode('utf-8'), dest=pdf_io, encoding="utf-8")

        pdf_io.seek(0)
        pdf_io.seek(0)
        return send_file(
            pdf_io,
            attachment_filename="차량정보.pdf".format(
                datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            ),
            as_attachment=True,
            cache_timeout=0,
            mimetype='application/pdf'
        )

    @route('/car/image/popup/', methods=['GET', 'POST'])
    def car_image_popup(self):
        try:
            car_id = request.args.get('car_id')
            car = Car.query.get(car_id)
            item = []

            for image in car.car_image_upload_file:
                item.append({'src': image.preview_url, 'title': '{} 사진'.format(car.name)})

            return json.dumps({
                'success': True,
                'item': item
            })

        except Exception as e:
            print(e)
            return json.dumps({'success': False})

