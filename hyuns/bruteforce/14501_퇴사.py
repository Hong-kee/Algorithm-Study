n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 생각해야할 점.  
# 1) 퇴사 전까지 상담받았을 때, 최대 금액  
# 2) 하나씩 dfs 이용해서 최대 상담 금액 result에 저장  
# 3) 마지막 일에 t=1일 경우도 가능

# 생각할 때 막히는 부분  
# 1) list에서 index는 0부터 시작하기 때문에 실제 값과 index가 다르다. 이것 때문에 계속 헷갈렸던 것 같다. -> 실제 모든 값에서 -1만큼 해주고 생각해야할 것 같다.  
# 2) 슬라이싱 이용해서 dfs를 돌렸는 데, T를 넣어주면서 현재 index 범위가 바뀌어서 헷갈려졌다.  
# 3) idx+t를 했을 때, 그 날이 퇴사날일 경우 포함시켜줘야 하는가? 아닌가?  
# -> 포함시켜줘야 한다. 생각해보면 T는 '오늘부터 상담 가능일'이기 때문에 오늘 상담이 가능하다. 따라서 
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