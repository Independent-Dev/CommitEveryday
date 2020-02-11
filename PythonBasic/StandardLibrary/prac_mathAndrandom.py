import math, random

print("-----math 모듈-----")
print("pi: ", math.pi)
print("e: ", math.e)
print("radian for 60\': ", math.radians(60))
print("degree for 1 radian: ", math.degrees(1))
print("밑이 3이고 진수가 9인 로그: ", math.log(9, 3))
print("그외: sin(number), cos(number), tan(number), exp(number)(지수함수 계산 함수) 등...")
print()
print("-----random 모듈-----")
print("1~10까지의 랜덤 정수: ", random.randint(1, 10))
print("1~10 사이 홀수: ", random.randrange(1, 10, 2))
#randrange(시작, 끝(포함), 증가분)으로 홀짝을 구할 수 있음.
print("1~10까지의 랜덤 실수: {:.4}".format(random.uniform(1, 10)))
print("0~1사이의 실수: {:.4}".format(random.random()))
animals = [('고양이', '삼모'), ('개', '코기'), ('고양이', '샴'), ('개', '닥스'), ('개', '흑러브')]
print("animals = ", animals)
print("animals에서 랜덤 요소 추출: ")
print(random.choice(animals))
print("animals에서 임의의 x개 뽑기!!: ", random.sample(animals, random.randint(1, len(animals))))
print("animals 섞기!!")
random.shuffle(animals)
print("결과: ", animals)




