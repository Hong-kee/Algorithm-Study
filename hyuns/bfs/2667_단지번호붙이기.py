from collections import deque
n = int(input())
graph= []

visited = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    ans = 1
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
            mx, my = x+i, y+j
            if mx >= 0 and my >= 0 and mx < n and my < n:
                if visited[mx][my] == False and graph[mx][my] == 1:
                    ans += 1
                    visited[mx][my] = True
                    q.append([mx, my])
    return ans

result = [0]
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0 and visited[i][j] == False:
            visited[i][j] = True
            result[0] += 1
            result.append(bfs(i, j))

result[1:] = sorted(result[1:])
for i in result:
    print(i)