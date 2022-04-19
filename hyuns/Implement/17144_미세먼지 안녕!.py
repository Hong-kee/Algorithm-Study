import sys

input = sys.stdin.readline


def spread_dust(arr, spread_arr):

    for dust_x in range(r):
        for dust_y in range(c):
            dust_amount = arr[dust_x][dust_y] // 5
            area_cnt = 0
            if graph[dust_x][dust_y] > 0 and visit[dust_x][dust_y] and dust_amount != 0:
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                    mx, my = dust_x + dx, dust_y + dy

                    if 0 <= mx < r and 0 <= my < c and arr[mx][my] != -1:
                        area_cnt += 1
                        spread_arr[mx][my] += dust_amount

                arr[dust_x][dust_y] = arr[dust_x][dust_y] - (dust_amount * area_cnt)


def move_dust(arr, mch_x, mch_y, direction):

    # 오른쪽 방향
    before_dust = 0
    start_x, start_y = mch_x, mch_y
    for dy in range(start_y + 1, c):
        start_y = dy
        tmp = arr[start_x][start_y]
        arr[start_x][start_y] = before_dust
        before_dust = tmp

    # 위 or 아래 방향
    last_x = -1 if direction == -1 else r
    for dx in range(start_x + direction, last_x, direction):
        start_x = dx
        tmp = arr[start_x][start_y]
        arr[start_x][start_y] = before_dust
        before_dust = tmp

    # 왼쪽 방향
    for dy in range(start_y-1, -1, -1):
        start_y = dy
        tmp = arr[start_x][start_y]
        arr[start_x][start_y] = before_dust
        before_dust = tmp

    # 위 or 아래 방향
    for dx in range(start_x - direction, mch_x, -direction):
        start_x = dx
        tmp = arr[start_x][start_y]
        arr[start_x][start_y] = before_dust
        before_dust = tmp


def cnt_dust():
    cnt = 0
    for dust_x in range(r):
        for dust_y in range(c):
            if graph[dust_x][dust_y] > 0:
                cnt += graph[dust_x][dust_y]
    return cnt


def add_graph(arr):
    for dust_x in range(r):
        for dust_y in range(c):
            arr[dust_x][dust_y] += spread_graph[dust_x][dust_y]


if __name__ == "__main__":
    r, c, t = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(r)]

    machine_coord = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                machine_coord.append([i, j])
        if len(machine_coord) == 2:
            break

    while t:
        t -= 1
        visit = [[False] * c for _ in range(r)]
        spread_graph = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    visit[i][j] = True

        spread_dust(graph, spread_graph)
        add_graph(graph)
        direct = -1

        for x, y in machine_coord:
            move_dust(graph, x, y, direct)
            direct = 1

    print(cnt_dust())
