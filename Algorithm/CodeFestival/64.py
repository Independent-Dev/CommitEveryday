target = int(input())
count = target//7
while count>=0:
    temp = target-7*count
    if temp%3==0:
        print(count+temp//3)
        break
    count-=1
else:
    print(-1)
