L, C = map(int, input().split())
data = input().split()
M = ['a','e','i','o','u']
result = []

data.sort()

# 모음은 적어도 한 개이상, 자음은 2개 이상
# 알파벳은 증가하는 순서로
# 정답 알파벳은 총 L 개수

def dfs(idx, ans, num_m):
    global result
    
    if len(ans) == L:
        if num_m >= 1 and (L-num_m) >= 2:
            result.append("".join(ans))
        return

    for i in range(idx, C):
        flag = True
        if data[i] in M:
            flag = False
            num_m += 1
        ans.append(data[i])
        dfs(i+1, ans, num_m)
        ans.remove(data[i])
        if not flag:
            num_m -= 1

ans = []
dfs(0, ans, 0)
for res in result:
    print(res)