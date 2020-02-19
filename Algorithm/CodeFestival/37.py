li = [x for x in input().split(" ")]
mx = 0

for x in li:
    if li.count(x) > mx:
        mx = li.count(x)
        student = x
print(f"{ student }가 { mx }표로 당선되었습니다^^") # this is f-string!!

#https://bluese05.tistory.com/70   "python3에서는 f-string이 갑이다."