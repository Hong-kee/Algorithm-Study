import sys
N = int(sys.stdin.readline()) # 토핑 종류의 수
A, B = map(int, sys.stdin.readline().split()) # A = 도우의 가격, B = 토핑 가격
dow_kcal = int(sys.stdin.readline()) # 도우의 열량
toping_kcal = []
cnt = 1


for _ in range(N):
    k = int(sys.stdin.readline()) # 토핑의 열량 (토핑 종류의 수 만큼 입력)
    toping_kcal.append(k)

toping_kcal.sort(reverse=True)

total_kcal = dow_kcal // A

for i in toping_kcal:
    if ((dow_kcal+i) // (A+B*cnt)) >= total_kcal:
        total_kcal = (dow_kcal+i) // (A+B*cnt)
        dow_kcal += i
        cnt += 1
    else:
        continue

print(total_kcal)


