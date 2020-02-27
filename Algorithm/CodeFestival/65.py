a = input("a: ")
b = input("b: ")
result = []
for x in range(len(a)):
    if x%2==0:
        result.append([a[x], b[x]])
    else:
        result.append([b[x], a[x]])
print(result)

result1 = [[a[x], b[x]] if x%2==0 else [b[x], a[x]] for x in range(len(a)) if x%2==0]
print(result1)