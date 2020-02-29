n = int(input("input : "))
count = int((n*2)**0.5)
result = n-count*(count-1)/2

if result > count:
    count+=1
    result = n - count * (count - 1) / 2

print(f'output : {int(result)}, {count+1}')