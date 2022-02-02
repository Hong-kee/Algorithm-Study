a, b = map(int, input().split())

cnt = 1
while b != a:
    cnt += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    
    if temp == b:
        cnt = -1
        break

print(cnt)