import sys, random
print("----sys모듈----")
print("파이썬 실행 명령의 인수 출력: ", sys.argv[1:])
print("파이썬 명령어의 path: ", sys.path)
print("현재의 default 인코딩: ", sys.getdefaultencoding())

#무한루프
while True:
    #target = random.ranint(1, 10)
    target = sys.stdin.readline()
    #target = target.strip("\n")
    sys.stdout.write(target)
    sys.stdout.flush()
    if int(target)%10==0:
        print("파이썬 종료!!")
        sys.exit(0)
