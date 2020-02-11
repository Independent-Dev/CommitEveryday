import bisect
import random

a = []
for _ in range(30):
    ran = random.randint(1, 20)
    print(ran)
    print(bisect.bisect_left(a, ran))
    #ran이 a에 정렬된 채로 삽입될 때의 인덱스를 반환함.
    bisect.insort_left(a, ran)
    print(a)
    print("--------")
