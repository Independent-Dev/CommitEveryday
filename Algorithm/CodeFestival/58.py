target = input()
result = target[-3:]
z = len(target)-3
while z > 0:
    temp = target[z-3:z]+","
    result = temp+result
    z-=3
result = target[:z+3]+result
print(result)

#함수를 사용하는 방법
target = int(target)
print(format(target, ","))#문자열 메소드 format()과는 다른 내장함수 format()

