n = input()
data = list(map(int, input().split()))
data.sort()
max, ans = sum(data), 0

for i in data:
    if i-ans > 1: # 부분 수열과 다음 max 값을 비교
        ans += 1
        break
    ans += i

if ans == max:
    print(ans+1)
else:
    print(ans)