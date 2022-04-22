import sys
# sys.stdin = open("input_13460.txt", "r")

# T = int(input())


def find_ball(arr):
    red_x, red_y, blue_x, blue_y = -1, -1, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "B":
                blue_x, blue_y = i, j
            elif arr[i][j] == "R":
                red_x, red_y = i, j
    return red_x, red_y, blue_x, blue_y


def lean_right(arr):

    rx, ry, bx, by = find_ball(arr)

    if ry >= by:  # Red가 우선 움직임.
        rang = (rx, ry), (bx, by)
    else:
        rang = (bx, by), (rx, ry)

    for (sx, sy) in rang:
        while True:
            sy += 1
            if arr[sx][sy] == "#" or arr[sx][sy] == "B" or arr[sx][sy] == "R":
                break
            elif arr[sx][sy] == "O":
                arr[sx][sy-1] = "."
                break
            arr[sx][sy], arr[sx][sy-1] = arr[sx][sy-1], "."


def lean_bottom(arr):

    rx, ry, bx, by = find_ball(arr)

    if rx >= bx:  # Red가 우선 움직임.
        rang = (rx, ry), (bx, by)
    else:
        rang = (bx, by), (rx, ry)

    for (sx, sy) in rang:
        while True:
            sx += 1
            if arr[sx][sy] == "#" or arr[sx][sy] == "B" or arr[sx][sy] == "R":
                break
            elif arr[sx][sy] == "O":
                arr[sx-1][sy] = "."
                break
            arr[sx][sy], arr[sx-1][sy] = arr[sx-1][sy], "."


def lean_left(arr):
    rx, ry, bx, by = find_ball(arr)

    if ry <= by:  # Red가 우선 움직임.
        rang = (rx, ry), (bx, by)
    else:
        rang = (bx, by), (rx, ry)

    for (sx, sy) in rang:
        while True:
            sy -= 1
            if arr[sx][sy] == "#" or arr[sx][sy] == "B" or arr[sx][sy] == "R":
                break
            elif arr[sx][sy] == "O":
                arr[sx][sy+1] = "."
                break
            arr[sx][sy], arr[sx][sy + 1] = arr[sx][sy + 1], "."


def lean_up(arr):
    rx, ry, bx, by = find_ball(arr)

    if rx <= bx:  # Red가 우선 움직임.
        rang = (rx, ry), (bx, by)
    else:
        rang = (bx, by), (rx, ry)

    for (sx, sy) in rang:
        while True:
            sx -= 1
            if arr[sx][sy] == "#" or arr[sx][sy] == "B" or arr[sx][sy] == "R":
                break
            elif arr[sx][sy] == "O":
                arr[sx+1][sy] = "."
                break
            arr[sx][sy], arr[sx + 1][sy] = arr[sx + 1][sy], "."


def check_result(arr):
    red_inArr, blue_inArr = False, False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "R":
                red_inArr = True
            elif arr[i][j] == "B":
                blue_inArr = True

    if not blue_inArr:
        return 0
    elif not red_inArr:
        return 1
    else:
        return 2


def dfs(arr, cnt, direct):
    global answer

    if cnt >= 10:
        return
    origin_arr = [item[:] for item in arr]  # deep copy
    for i in range(4):
        if i == 0 and i != direct and direct != 2:
            lean_right(arr)
        elif i == 1 and i != direct and direct != 3:
            lean_bottom(arr)
        elif i == 2 and i != direct and direct != 0:
            lean_left(arr)
        elif i == 3 and i != direct and direct != 1:
            lean_up(arr)

        hole = check_result(arr)
        if hole == 0 or arr == origin_arr:  # fail
            pass
        elif hole == 1:  # success
            answer = min(answer, cnt + 1)
            return
        else:
            dfs(arr, cnt + 1, i)

        arr = [item[:] for item in origin_arr]


if __name__ == "__main__":  # for test_case in range(T):
    N, M = map(int, input().split())
    graph = []
    R_d, B_d = [], []
    answer = N * N

    for row in range(N):
        st = input()
        ele_graph = []
        for col in range(len(st)):
            ele_graph.append(st[col])
            if st[col] == "R":
                R_d = [row, col]
            elif st[col] == "B":
                B_d = [row, col]
        graph.append(ele_graph)

    dfs(graph, 0, -1)
    if answer == N * N:
        print(-1)
    else:
        print(answer)
