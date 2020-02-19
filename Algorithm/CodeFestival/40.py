target = int(input())
num = int(input())
temp = 0
li = []
for x in range(num):
    temp+=int(input())
    if target<temp:
        li.append(True)
    else:
        li.append(False)

print(li.index(True))
