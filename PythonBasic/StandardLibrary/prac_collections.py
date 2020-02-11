from collections import OrderedDict
od = OrderedDict()
od['a'] = 'A'
od['c'] = 'C'
od['b'] = 'B'

print("----1.OrderedDict----")
print("""od = OrderedDict()
od['a'] = 'A'
od['c'] = 'C'
od['b'] = 'B'""")
print(od)

print()

Dict = {}
Dict['a'] = 'A'
Dict['c'] = 'C'
Dict['b'] = 'B'
print("""Dict = {}
Dict['a'] = 'A'
Dict['c'] = 'C'
Dict['b'] = 'B'""")
print("Dict: ", Dict)

from collections import defaultdict
print("----2-1.defaultdict----")
animals = [('고양이', '삼모'), ('개', '코기'), ('고양이', '샴'), ('개', '닥스'), ('개', '흑러브')]
dd = defaultdict(list)
for k, v in animals:
    dd[k].append(v)
print(dd)

print("----2-2.normal dict----")
nd = {}
try:
    for k, v in animals:
        nd[k].append(v)
    print(nd)
except KeyError as e:
    print("에러가 발생했습니다")
    print(e)
