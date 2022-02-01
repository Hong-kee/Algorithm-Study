s1, s2= input(), input()
answer = 0

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(answer)