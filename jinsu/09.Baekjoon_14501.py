n = int(input())
t = []  # 기간 리스트
p = []  # 금액 리스트
dp = [] # dp 테이블 리스트

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)

for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])