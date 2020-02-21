inp = input()
li = []
for i in inp[:]:
    if i =="(":
        li.append(i)
    elif i==")" and len(li)==0:
        print("NO")
        break
    elif i==")":
        li.pop()
else:
    if len(li)>0:
        print("NO")
    else:
        print("YES")
