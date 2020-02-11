import re
p = re.compile('[a-z]+')

print("-----match 메소드: target = 'python'-----")
m = p.match("python")
print(m)

print("-----match 메소드: target = '3 python'-----")
m1 = p.match("3 python")
print(m1)

print("활용방법-target = 'python'")
if m:
    print("Match found: ", m.group())
else:
    print("no Match")

print("활용방법-target = '3 python'")
if m1:
    print("Match found: ", m.group())
else:
    print("no Match")

print("-----search 메소드-----")
s = p.search("3 python")
print(s)

print("-----findall 메소드: target = 'life is too short'-----")
target = "life is too short"
f = p.findall(target)
print(f)

print("-----finditer 메소드: target = 'life is too short'-----")
f1 = p.finditer(target)
for x in range(len(p.findall(target))):
    print(next(f1).group())

# f1 = p.finditer("life is too short")
# try:
#     while True:
#         print(next(f1).group())
# except:
#     print("f1 끝")

print()
print("----match 객체 메소드: start(), end(), span()----")
print("start(): ", s.start())
print("end(): ", s.end())
print("span(): ", s.span())
