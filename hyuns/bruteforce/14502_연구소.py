from itertools import combinations
from collections import deque
from copy import deepcopy as dc
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_zero(graph_c):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph_c[i][j] == 0:
                cnt += 1
    return cnt

def wall_dir(can_wall_graph):
    return list(combinations(can_wall_graph, 3))

def solution(graph, n, m):
    
    answer = 0
    can_wall_graph, where_two = [], []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                can_wall_graph.append([i, j])
            if graph[i][j] == 2:
                where_two.append([i, j])
                

    for [x1, y1], [x2,y2], [x3, y3] in wall_dir(can_wall_graph):
        graph_c = dc(graph)
        graph_c[x1][y1], graph_c[x2][y2], graph_c[x3][y3] = 1, 1, 1

        q = deque()
        for x, y in where_two:
            q.append([x, y])

        while q:
            x, y = q.popleft()
            for dx, dy in (1,0), (0,1), (-1,0), (0,-1):
                mx, my = x+dx, y+dy
                if mx >= 0 and my >= 0 and mx < n and my < m:
                    if graph_c[mx][my] == 0:
                        graph_c[mx][my] = 2
                        q.append([mx, my])
        
        answer = max(answer, check_zero(graph_c))

    return answer

print(solution(graph, n, m))