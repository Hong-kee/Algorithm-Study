from collections import deque
start, end = map(int, input().split())

def bfs(start, end):
    
    answer = 1

    x, y = 2*start, int(str(start)+"1")
    if x == end or y == end: # 처음 값 비교
        return answer + 1

    q = deque()
    q.append([x, answer+1])
    q.append([y, answer+1])
    while q:

        n, answer = q.popleft()
        
        x, y = n*2, int(str(n) + "1")
        if x == end or y == end:    # 같으면 return
            return answer + 1
        if x < end:                 # 작을 경우만 넣기
            q.append([x, answer+1])
        if y < end:
            q.append([y, answer+1])

    return -1

print(bfs(start, end))