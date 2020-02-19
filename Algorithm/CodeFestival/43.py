target = int(input())
result = ""
while target > 0:
    result = str(target % 2) + result # 파이썬에서는 서로 다른 자료형의 덧셈을 허용하지 않음.
    target //= 2
print(result)
