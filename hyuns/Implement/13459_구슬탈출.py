import sys
from collections import deque

input = sys.stdin.readline


def get_ballDirection():
    rx, ry, bx, by = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                rx, ry = i, j
            elif graph[i][j] == "B":
                bx, by = i, j
        if rx >= 0 and ry >= 0 and bx >= 0 and by >= 0:
            break

    return rx, ry, bx, by


def move_coord(arr, mx, my, dx, dy):
    dis = 0
    go_hole = False
    while arr[mx+dx][my+dy] != "#":
        if arr[mx+dx][my+dy] == "O":
            go_hole = True
            break
        mx += dx
        my += dy
        dis += 1
    return mx, my, dis, go_hole


def bfs(arr, red, blue):
    [rx, ry], [bx, by] = red, blue
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append([rx, ry, bx, by, 0, -99])

    while q:
        rx, ry, bx, by, cnt, direct = q.popleft()
        if cnt >= 10:
            continue
        for i in range(4):
            if abs(i-direct) == 2 or i == direct:
                continue

            mrx, mry, dis_r, red_inHole = move_coord(arr, rx, ry, dx[i], dy[i])
            mbx, mby, dis_b, blue_inHole = move_coord(arr, bx, by, dx[i], dy[i])

            if blue_inHole:
                continue
            elif red_inHole:
                return 1
            else:  # nothing's gonna happen
                if mrx == mbx and mry == mby:
                    # long's coord is on behind
                    if dis_r > dis_b:
                        mrx -= dx[i]
                        mry -= dy[i]
                    else:
                        mbx -= dx[i]
                        mby -= dy[i]
                q.append([mrx, mry, mbx, mby, cnt+1, i])
    return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    red_x, red_y, blue_x, blue_y = get_ballDirection()

    print(bfs(graph, [red_x, red_y], [blue_x, blue_y]))
