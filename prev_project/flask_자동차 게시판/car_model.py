# coding: utf-8

"""Database Model: Car"""
import os
from os import path

from app.models import db
from app.utils.define import CarColor, CarCategory, EnumYN, FillMethod, \
    CarPowerPlantDevice
from app.utils.uploads import FileConfigPathSupport, FileConfig, UploadGroup, \
    UploadTypes, FileConfigPathParam
import shortuuid
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.mysql import INTEGER

class CarBrand(db.Model):
    """Brand 정보"""
    __tablename__ = 'car_brand'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    code_country_id = db.Column(db.Integer, db.ForeignKey('code_country.id'), nullable=False)  # 브랜드 국가 코드
    code_country = db.relationship('CodeCountry', foreign_keys=code_country_id)
    registered_at = db.Column(db.DateTime(), nullable=False, index=True)  # 등록일

    car_brand_image_upload_file = db.relationship("CarBrandImageUploadFile", backref="car_brand_image_upload_file", uselist=False)


class Car(db.Model):
    """자동차 정보: 기본정보, 편의사항, 안전"""
    __tablename__ = 'car'
    __table_args__ = (
        db.UniqueConstraint('car_brand_id', 'name'),
    )

    # 기본 정보
    id = db.Column(db.Integer, primary_key=True)
    car_brand_id = db.Column(db.Integer, db.ForeignKey('car_brand.id'), nullable=False)
    car_brand = db.relationship('CarBrand', foreign_keys=car_brand_id, backref='car')
    name = db.Column(db.String(64), nullable=False, index=True)
    color = db.Column(db.Enum(CarColor), nullable=False)
    passenger_count = db.Column(INTEGER(unsigned=True), nullable=False)  # 탑승 인원
    category = db.Column(db.Enum(CarCategory), nullable=False, index=True)  # 분류
    released_at = db.Column(db.DateTime())  # 출시일
    power_plant_device = db.Column(db.Enum(CarPowerPlantDevice), nullable=False, index=True)  # 동력발생장치

    # 편의사항
    has_mobile_linkage = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 모바일 연동
    has_cruise_control = db.Column(db.Enum(EnumYN), index=True, default=EnumYN.N, server_default=EnumYN.N.name)  # 크루즈 컨트롤
    has_heated_stering_wheel = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 열선 스티어링 휠
    has_heated_sheet = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 열선 시트

    # 안전
    airbag_count = db.Column(INTEGER(unsigned=True), default=0, server_default='0')  # 에어백 갯수
    has_slope_safe = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 경사로 밀림 방지
    has_sudden_breaking_alarm = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 급제동 알림
    has_rear_sensor = db.Column(db.Enum(EnumYN), default=EnumYN.N, server_default=EnumYN.N.name)  # 후방 감지

    # 옵션
    option_list = db.Column(db.JSON(none_as_null=True))

    engine = db.relationship('Engine', backref="car", uselist=False)
    motor = db.relationship('Motor', backref="motor", uselist=False)
    car_image_upload_file = db.relationship("CarImageUploadFile", backref="car_image_upload_file", uselist=True)




class Engine(db.Model):
    """엔진 정보"""
    __tablename__ = 'engine'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False, unique=True)
    engine_shift = db.Column(INTEGER(unsigned=True), nullable=False)  # 엔진 변속 unsigned로 하면 양수 영역에서 쓸 수 있는 데이터가 2배 더 많아짐.
    is_automatic = db.Column(db.Enum(EnumYN), nullable=False)  # 자동 변속


class Motor(db.Model):
    """모터 정보"""
    __tablename__ = 'motor'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False, unique=True)
    fill_method = db.Column(db.Enum(FillMethod), nullable=False)  # 충전 방식
    boost_charge_time = db.Column(INTEGER(unsigned=True), nullable=False)  # 급속 충전 시간
    slow_charge_time = db.Column(INTEGER(unsigned=True), nullable=False)  # 완속 충전 시간


class CarImageUploadFile(db.Model, FileConfigPathSupport):  # file_path 등의 프로퍼티와 메소드를 제공..
    """CarHolder 업로드 파일"""
    __tablename__ = 'car_image_upload_file'
    __file_config__ = FileConfig(UploadGroup.CP, UploadTypes.CAR)  # 이건 uploads.py에 저장되어 있음.
    # 기본적으로 UPLOAD_ROOT_DIR 밑에 upload_group(UploadGroup)으로 디렉토리를 설정한다.
    # 새로운 값을 사용할 경우 nginx가 알 수 있게 설정에 등록해두어야 함.

    id = db.Column(db.Integer, primary_key=True)  # PK
    queue_suuid = db.Column(db.String(25), nullable=False)
    file_suuid = db.Column(db.String(25), nullable=False)
    file_base = db.Column(db.String(80), nullable=False)
    file_ext = db.Column(db.String(5), nullable=False)

    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)  # 등록자
    registered_at = db.Column(db.DateTime, nullable=False)  # 등록일

    @property
    def file_config_param(self):  # file_path와 같은 property의 리턴값인 get_path_for_file()의 인수로 사용됨.
        return FileConfigPathParam(
            file_at=self.registered_at,
            queue_suuid=self.queue_suuid,
            file_suuid=self.file_suuid,
            file_ext=self.file_ext
        )

    def delete_file(self):
        file_path = self.file_path  # 이와 같은 property를 쓸 수 있는 것은 이 클래스가 FileConfigPathSupport를 상속하기 때문임.
        if path.exists(file_path):
            os.remove(file_path)
            os.rmdir("/".join(file_path.split("/")[:-1]))
            print("원본 파일과 폴더가 정상적으로 삭제되었습니다.")

    def delete_thumb(self):
        thumb_path = self.thumb_path
        if path.exists(thumb_path):
            os.remove(thumb_path)
            os.rmdir("/".join(thumb_path.split("/")[:-1]))
            print("썸네일 파일과 폴더가 정상적으로 삭제되었습니다.")


    def delete_preview(self):
        preview_path = self.preview_path
        if path.exists(preview_path):
            os.remove(preview_path)
            os.rmdir("/".join(preview_path.split("/")[:-1]))
            print("프리뷰 파일과 폴더가 정상적으로 삭제되었습니다.")

    # attach_name, qquuid, uploaded_file_name은 삭제.

class CarBrandImageUploadFile(db.Model, FileConfigPathSupport):
    """CarHolder 업로드 파일"""
    __tablename__ = 'car_brand_image_upload_file'
    __file_config__ = FileConfig(UploadGroup.CP, UploadTypes.CAR)

    id = db.Column(db.Integer, primary_key=True)  # PK
    queue_suuid = db.Column(db.String(25), nullable=False)
    file_suuid = db.Column(db.String(25), nullable=False)
    file_base = db.Column(db.String(80), nullable=False)
    file_ext = db.Column(db.String(5), nullable=False)

    car_brand_id = db.Column(db.Integer, db.ForeignKey('car_brand.id'), nullable=False, unique=True)  # 해당 자동차 브랜드
    registered_at = db.Column(db.DateTime, nullable=False)  # 등록일

    @property
    def file_config_param(self):
        return FileConfigPathParam(
            file_at=self.registered_at,
            queue_suuid=self.queue_suuid,
            file_suuid=self.file_suuid,
            file_ext=self.file_ext
        )

    def delete_file(self):
        # Delete metadata file on disk
        file_path = self.file_path
        dir, _ = path.split(file_path)
        if path.exists(file_path):
            os.remove(file_path)
            os.rmdir(dir)

    def delete_thumb(self):
        # Delete metadata file on disk
        thumb_path = self.thumb_path
        dir, _ = path.split(thumb_path)
        if path.exists(thumb_path):
            os.remove(thumb_path)
            os.rmdir(dir)

    def delete_preview(self):
        preview_path = self.preview_path
        dir, _ = path.split(preview_path)
        if path.exists(preview_path):
            os.remove(preview_path)
            os.rmdir(dir)
