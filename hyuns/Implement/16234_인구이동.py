import sys
from collections import deque

input = sys.stdin.readline


def find_union(visit, nr, nc):
    union_flag = False
    single_unionPeople = 0
    single_union = []
    q = deque()

    q.append([nr, nc])
    visit[nr][nc] = True
    single_union.append([nr, nc])
    single_unionPeople += graph[nr][nc]
    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            mx, my = x + dx, y + dy
            if 0 <= mx < N and 0 <= my < N and not visit[mx][my]:
                if L <= abs(graph[mx][my] - graph[x][y]) <= R:
                    union_flag = True
                    q.append([mx, my])
                    visit[mx][my] = True
                    single_union.append([mx, my])
                    single_unionPeople += graph[mx][my]

    return union_flag, single_union, single_unionPeople // len(single_union)


def read_graphState(nation_graph):
    visit = [[False] * N for _ in range(N)]
    union = []
    after_union = []

    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                flag, u, au = find_union(visit, r, c)  # 좌표값, 변화값
                if flag:
                    union.append(u)
                    after_union.append(au)

    if union:
        for idx in range(len(union)):
            for x, y in union[idx]:
                nation_graph[x][y] = after_union[idx]
        return True

    return False


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    day = 0
    while read_graphState(graph):
        day += 1

    print(day)
