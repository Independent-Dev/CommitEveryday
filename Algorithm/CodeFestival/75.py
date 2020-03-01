target = input()
result = 0
for i, n in enumerate(target):
    result = result*3+int(n)//3
    if int(n)%3!=0:
        for x in range(1, len(target)-i):
            result = result*3 + 3
        break

print(result)