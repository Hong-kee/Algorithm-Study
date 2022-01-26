n = int(input())
data = [input() for _ in range(n)]
result = 0

for st in data:
    ch = [st[0]]
    flag = True
    for i in range(1, len(st)):
        if ord(st[i]) != ord(st[i-1]):
            if st[i] in ch:
                flag = False
                break
            else:
                ch.append(st[i])
    if flag:
        result += 1

print(result)
