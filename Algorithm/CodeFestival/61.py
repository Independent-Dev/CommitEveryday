target = input()+" "
result = target[0]
count = 1
for x in range(len(target)-1):
    if target[x]==target[x+1]:
        count+=1
    else:
        result = result+str(count)+target[x+1]
        count = 1
print("/"+result.strip()+"/")