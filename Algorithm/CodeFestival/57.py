# li = [str(x) for x in range(1001)]
# target = "".join(li)
# print(target.count("1"))

def C(number):
    result = str(list(range(number+1))).count("1")
    return result

print(C(1000))