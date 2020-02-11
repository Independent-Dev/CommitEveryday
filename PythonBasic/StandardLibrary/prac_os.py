import os
print("----프로세스 정보 취득 및 조작----")
print(os.environ)
print(os.getenv('TERM_PROGRAM'))

print("----파일, 디렉토리 조작----")
print("기존의 파일/디렉토리 목록")
print(os.listdir(os.getcwd()))

target = input("생성할 디렉토리 명: ")
os.mkdir("./"+target+"/")

print("방금 생성한 것은 파일인가? ", os.path.isfile("./"+target+"/"))

print("방금 생성한 것은 디렉토리인가? ", os.path.isdir("./"+target+"/"))

print("생성 후 파일/디렉토리 목록")
print(os.listdir(os.getcwd()))

print("생성한 디렉토리로 이동")
os.chdir("./"+target+"/")

print("현재 경로: ", os.getcwd())

print("경로 변경: 만든 디렉토리+'1'")
os.rename(os.getcwd(), "../"+target+"1/")
print("결과: ", os.getcwd())

print("상위 디렉토리로!")
os.chdir("..")

print("방금 생성한 디렉토리가 현재 디렉토리 내에 존재하나?: ", os.path.exists("./"+target+"1/"))
print("생성한 디렉토리 삭제")
os.rmdir("./"+target+"1/")

print("여전히 존재하나?: ", os.path.exists("./"+target+"1/"))
print("삭제 후 파일/디렉토리 목록")
print(os.listdir(os.getcwd()))

print("파일 "+target+".txt 생성")
path1 = os.path.join("./", target+".txt")
os.system("touch "+ path1)

print(os.listdir(os.getcwd()))

print("파일 "+target+".txt 삭제")
os.remove(path1)

print(os.listdir(os.getcwd()))

print("----프로세스 관리(mac에서는 startfile()은 실행 안 됨)----")
print("prac_sys.py파일 실행!!")
os.system("python prac_sys.py 1, 2, 3")
