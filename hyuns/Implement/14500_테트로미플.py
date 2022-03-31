
import sys
input = sys.stdin.readline

def search_max(i, j, idx, value, visit):
    global answer
    if answer > value + max_value * (3-idx):
        return
    if idx == 3:
        answer = max(answer, value)
        return

    for di, dj in move:
        mi, mj = i+di, j+dj
        if 0 <= mi < N and 0 <= mj < M and visit[mi][mj] == False:
            visit[mi][mj] = True
            search_max(mi, mj, idx+1, value+graph[mi][mj], visit)
            visit[mi][mj] = False
    return

def search_rest(i, j):
    global answer
    sum_value = graph[i][j]
    cnt = 0
    for di, dj in move:
        mi, mj = i+di, j+dj
        if 0 <= mi < N and 0 <= mj < M:
            cnt += 1
            sum_value += graph[mi][mj]
    if cnt == 3:
        answer = max(sum_value, answer)
    elif cnt == 4:
        answer = max(answer, max([sum_value - graph[i+move[k][0]][j+move[k][1]] for k in range(4)]))

    return

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
max_value = max(map(max, graph))
move = [(0,1), (1,0), (0,-1), (-1,0)]
answer = -1

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        search_max(i, j, 0, graph[i][j], visit)
        search_rest(i, j)
        visit[i][j] = False

print(answer)