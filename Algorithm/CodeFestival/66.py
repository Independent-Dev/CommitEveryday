target = input().split("/")
rule = input()
result = []
for string in target:
    count = 0
    for ch in string[:]:
        print(ch)
        if ch in rule:
            print(rule.index(ch))
            if rule.index(ch) < count:
                result.append("불가능")
                break
            else:
                count = rule.index(ch)
    else:
        result.append("가능")

print(result)