target = input()
target1 = target.split(" ")
result = ""
for letter in target1:
    result+=letter[0]
print(result)

target2 = [x[0] for x in target.split(" ")]
print("".join(target2))