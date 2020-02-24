#바보 같은 풀이1
temp = input()
temp1 = temp
while len(temp)<50:
    temp = "="+temp+"="

print(temp)

half2 = temp1[int(len(temp)/2):].ljust(5, "=")
half1 = temp1[:int(len(temp)/2)].rjust(5, "=")
print(half1+half2)
