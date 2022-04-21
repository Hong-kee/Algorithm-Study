import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


def bfs():
    hx, hy = graph[0]
    lx, ly = graph[-1]
    visited = [False] * n
    q = deque()
    q.append([hx, hy])
    while q:
        nx, ny = q.popleft()
        if abs(lx-nx) + abs(ly-ny) <= 1000:
            print("happy")
            return
        for idx, (cx, cy) in enumerate(graph[1:-1]):
            if abs(cx-nx) + abs(cy-ny) <= 1000 and not visited[idx]:
                visited[idx] = True
                q.append([cx, cy])
    print("sad")
    return


for test_case in range(T):
    n = int(input())
    graph = []
    for _ in range(n+2):
        graph.append(list(map(int, input().split())))

    bfs()