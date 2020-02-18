li = [int(x) for x in input().split(" ")]
# tOrF = [[False for x, y in li[z:z+2] if x>y] for z in range(len(li)-1)]
tOrF = [False for z in range(len(li)-1) if li[z]>li[z+1]] 
if False in tOrF:
    print("NO")
else:
    print("yes")
