mon = [1, -1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
d = ["TUE", "WED", "THU", "FRI", "SAT", "SUN", "MON"]
a = int(input())
b = int(input())
result = (a-1) * 30 + sum(mon[:a-1]) + b
print(d[result%7])
