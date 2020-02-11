import datetime

print("-------datetime.datetime 클래스-------")
dt = datetime.datetime.now()
#위와 같은 방식으로 객체를 생성하여 이용 가능.
print("현재 시각: ", dt)
print("요일: ", dt.weekday)
print("이번 달: ", dt.month)

print("-------datetime.date 클래스-------")
dt1 = datetime.date.today()
#위와 같은 방식으로 객체를 생성하여 이용 가능.
print("올해: ", dt1.year)
print("오늘 날짜: ", dt1.day)

print("-------datetime.time 클래스-------")
dt2 = datetime.time(10, 20)
#시, 분, 초, 밀리초를 인수로 설정 가능.
print("시각: ", dt2.hour)
print("분: ", dt2.minute)


print("-------이상의 클래스들은 strftime() 메소드를 통해 날짜와 시간을 원하는 방식으로 포맷하여 문자열을 얻을 수 있음-------")
print(dt.strftime("%A %d. %B %Y"))
#위 포멧 방식은 자주 이용할 것 같다. 더 공부해 볼 것.

print("-------datetime.timedelta 클래스-------")
#날짜와 시간차를 보다 쉽게 취급할 수 있게 도와주는 클래스
print("1)datetime객체의 차")
dt1 = datetime.datetime(2016, 2, 19, 14)
dt2 = datetime.datetime(2016, 1, 2, 13)
td = dt1 - dt2
print("2016.2.19 14시-2016.1.2 13시 = ", td)
print("일수: ", td.days)

print("2)datetime 객체와 timedelta 객체의 연산")
td1 = datetime.timedelta(100)
print("2016.1.2 13시+100일 = ", dt2+td1)

print("---------calendar 모듈---------")
import calendar
print("올해 3월 1은 무슨 요일일까??(ex:0 = 월요일...6 = 일요일)", calendar.weekday(2020, 3, 1))
print("올해 4월 달력 출력!!")
print(calendar.month(2020, 4))
print("올해는 윤년일까?!? ", calendar.isleap(2020))
