import csv
from io import StringIO
import os

tem_string = "일종의 파일을 흉내내는 객체. 문자열 데이터를 파일로 저장한 다음 여러가지 처리를 하게 되는데, 그 파일이 다시 쓰이지 않을 때 유용함. 처리 과정에서 동적으로 파일의 확장자나 내용이 바뀌는 데이터(파일)에서도 유용할 거라고 생각함. "
tem_list = tem_string.split(" ")
pre_csv = ", ".join(tem_list)
f = StringIO(pre_csv)

os.system("echo '"+pre_csv+"' > pre.csv")
#pre.csv 파일 만들기

csvFile = open("pre.csv", encoding="utf-8")

for row in csv.reader(csvFile):
    print(row)

csvFile.close()

# import sys
# sys.exit()
f = open("pre.csv", "w", encoding='utf-8')
W = csv.writer(f)
temp_list = []
while True:
    temp = input("아무거나 입력하세요. 0은 종료\n")

    print(temp_list)
    if temp == "0":
        temp_list.append(temp)
        break
    temp_list.append(temp)

W.writerows(temp_list)
f.close()
csvFile = open("pre.csv", encoding="utf-8")
it = csv.reader(csvFile)
for row in csv.reader(csvFile):
    print(row)
# try:
#     while 1:
#         a = next(it)
#         print(a)
#
# except:
#     print("csv 파일 끝")
