target = int(input())
for i in range(2, int(target**0.5)+1):
    if target%i==0:
        print("NO")
        break
else:
    if target == 1:
        print("NO")
    else:
        print("YES")