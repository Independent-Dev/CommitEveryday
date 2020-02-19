num = int(input())
li = [print(num*x, end=" ") for x in range(1, 10)]
# 이게 들어가지 않으면 "2 4 6 8 10 12 14 16 18 %" 처럼 뒤에 하나가 더 찍힘. 
print()