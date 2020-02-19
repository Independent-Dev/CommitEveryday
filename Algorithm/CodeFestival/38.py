import bisect

li = [int(x) for x in input().split(" ")]
li.sort(reverse=True)
count = 0
for x in range(len(li)-1):
    if li[x] > li[x+1]:
        count += 1
    if count >= 3:
        print(x+1)
        print(li)
        break
