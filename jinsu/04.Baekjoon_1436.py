n = int(input())
cnt = 0
si = 666
while True:
    if '666' in str(si):
        cnt += 1
    if n == cnt:
        print(si)
        break
    si += 1
    