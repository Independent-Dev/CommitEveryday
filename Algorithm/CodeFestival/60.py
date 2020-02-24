li = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
li1 = [[index+1, x] for index, x in enumerate(li)]
for index, name in li1:
    print(f"번호: {index} 이름: {name}")