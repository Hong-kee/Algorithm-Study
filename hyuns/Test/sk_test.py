# def solution(money, costs):
#     answer = 0
#     return answer


# money = 4578
# costs = [1, 4, 99, 35, 50, 1000]


# clockwise

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    
    if clockwise == True:        
        for j in (0, n-1, n-1, 0):
            numb = 0
            k_n = n
            dir = 0 # left to right
            start = 0
            while k_n >= 1:
                if dir == 0:
                    if k_n == 1:
                        answer[j][start] = numb + 1
                    for i in range(start, start + k_n-1):
                        numb += 1
                        answer[j][i] += numb
                    start = j + 1
                elif dir == 1:
                    if k_n == 1:
                        answer[start][j] = numb + 1
                    for i in range(start, start + k_n-1):
                        numb += 1
                        answer[i][j] += numb
                    start = j - 1
                elif dir == 2:
                    if k_n == 1:
                        answer[j][start] = numb + 1
                    for i in range(start, start - k_n-3, -1):
                        numb += 1
                        answer[j][i] += numb
                    start = j - 1
                elif dir == 3:
                    if k_n == 1:
                        answer[start][j] = numb + 1
                    for i in range(start, start - k_n-3, -1):
                        numb += 1
                        answer[i][j] += numb
                    start = j + 1
                
                j = k_n-2
                dir += 1
                if dir == 4:
                    dir = 0
                k_n -= 2
                if k_n == 0:
                    k_n = 1

        
    return answer

n = 5 # 4 + 2 + 1
        # n=6, 5 + 3 + 2

clockwise = True
print(solution(n, clockwise))


# 간선
from collections import deque
from itertools import permutations
def solution(n, edges):
    answer = 0
    distance = [[0] * n for _ in range(n)]               
    graph = [[] for _ in range(n)]
    
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[0]].sort()
        graph[e[1]].append(e[0])
        graph[e[1]].sort()

    q = deque()
    for i in range(n):
        q.append(i)
        visit = [False] * n
        while q:
            node = q.popleft()
            visit[node] = True
            for nd in graph[node]:
                if i==nd or visit[nd]:
                    continue
                distance[i][nd] = distance[i][node] + 1
                distance[nd][i] = distance[i][nd]
                q.append(nd)

    for i, j, k in permutations(range(0, n), 3):
        if distance[i][j] == 0 or distance[j][k] == 0 or distance[i][k] == 0:
            continue
        if (distance[i][j] + distance[j][k]) == distance[i][k]:
            answer += 1

    return answer

n=4
edges = [[2,3],[0,1],[1,2]]
print(solution(n,edges))