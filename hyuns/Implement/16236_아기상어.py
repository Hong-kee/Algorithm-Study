import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, arr):
    global shark_size
    min_t = N * N
    last_x, last_y = x, y
    last_pos = []
    q = deque()

    visit = [[False] * N for _ in range(N)]
    visit[x][y] = True
    q.append([x, y, 0])

    while q:
        nx, ny, mt = q.popleft()
        for i in range(4):
            mx, my = nx + dx[i], ny + dy[i]
            if 0 <= mx < N and 0 <= my < N and arr[mx][my] <= shark_size[0] and not visit[mx][my]:
                visit[mx][my] = True
                if 0 < arr[mx][my] < shark_size[0]:
                    min_t = mt + 1
                    last_pos.append([min_t, mx, my])
                if mt + 1 <= min_t:
                    q.append([mx, my, mt + 1])

    if last_pos:
        t, last_x, last_y = sorted(last_pos)[0]
        graph[x][y] = 0
        graph[last_x][last_y] = 9
        shark_size[1] += 1
    else:
        t = 0

    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0

    return t, last_x, last_y


if __name__ == "__main__":

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    sx, sy, flag = 0, 0, False
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                sx, sy = i, j
                flag = True
                break
        if flag:
            break

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    shark_size = [2, 0]  # [size, eat]
    time = 0
    while True:
        eat_time, lx, ly = bfs(sx, sy, graph)
        if eat_time == 0:
            break
        else:
            time += eat_time
            sx, sy = lx, ly

    print(time)