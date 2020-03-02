target = int(input())
if target == 1:
    result = int((target / 3)**0.5)
    while target - (3 * (result - 1) * result + 1) >= 0:
        result += 1

print(result)
