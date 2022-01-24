n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 퇴사 전까지 상담받았을 때, 최대 금액
# 하나씩 dfs 이용해서 최대 상담 금액 result에 저장
# 마지막 일에 t=1일 경우도 가능

# 생각할 때 막히는 부분
# 1) list에서 index는 0부터 시작하고 n은 전체 크기일 때, 서로 더했을 경우 그 위치 -> 실제 값에서 -1만큼 해주고 생각하자.
# 2) 슬라이싱 이용하려 했는데, 그거 이용하니까 index 범위가 바뀌어서 더 헷갈림
# 3) idx를 더했을 때, 그 날이 퇴사날일 경우 포함시켜줘야 하는가? 아닌가? -> 포함
# 4) recursion function은 이해하겠는데, 적용시키려니까 잘 안됨

def dfs(idx, ans):

    global result
    if idx >= n: # 퇴사 날일 경우
        result = max(result ,ans)
        return
    
    for i in range(idx, len(data)):
        t, p = data[i]
        
        if t+i >= n+1: # 더했을 때, 퇴사 날을 넘어설 경우
            dfs(t+i, ans)
        if t+i <= n: # 더했을 때, 퇴사 날일 경우까지
            dfs(t+i, ans+p)
        
dfs(0, 0)
print(result)