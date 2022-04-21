import sys
from collections import deque

input = sys.stdin.readline


def move_rl(arr, direct):
    max_num = 0
    for fix in range(N):
        tmp_arr = arr[fix][:]
        ch_arr = []
        start = 0

        if direct == 0:
            tmp_arr = tmp_arr[::-1]

        for y in range(N):
            if tmp_arr[y] > 0:
                if start == 0 or start != tmp_arr[y]:
                    ch_arr.append(tmp_arr[y])
                    start = tmp_arr[y]
                elif start == tmp_arr[y]:
                    ch_arr[-1] += tmp_arr[y]
                    start = 0

        for rest_zero in range(N - len(ch_arr)):
            ch_arr.append(0)

        if direct == 0:
            ch_arr = ch_arr[::-1]

        arr[fix] = ch_arr[:]
        max_num = max(max(ch_arr), max_num)

    return max_num


def move_ud(arr, direct):
    max_num = 0
    for fix in range(N):
        tmp_arr = []
        for x in range(N):
            tmp_arr.append(arr[x][fix])
        ch_arr = []
        start = 0

        if direct == 1:
            tmp_arr = tmp_arr[::-1]

        for x in range(N):
            if tmp_arr[x] > 0:
                if start == 0 or start != tmp_arr[x]:
                    ch_arr.append(tmp_arr[x])
                    start = tmp_arr[x]
                elif start == tmp_arr[x]:
                    ch_arr[-1] += tmp_arr[x]
                    start = 0

        for rest_zero in range(N - len(ch_arr)):
            ch_arr.append(0)

        if direct == 1:
            ch_arr = ch_arr[::-1]

        max_num = max(max(ch_arr), max_num)
        for x in range(N):
            arr[x][fix] = ch_arr[x]

    return max_num


def count_arr(arr):
    mx = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                mx = max(arr, mx)
    return arr


def bfs(arr):
    global answer
    q = deque()
    c_arr = [item[:] for item in arr]
    q.append([c_arr, 0, -1])

    while q:
        c_arr, cnt, mx = q.popleft()
        if cnt == 5:
            answer = max(mx, answer)
            continue
        origin_arr = [item[:] for item in c_arr]
        for i in range(4):
            if i == 0 or i == 2:
                mx = max(mx, move_rl(c_arr, i))
            else:
                mx = max(mx, move_ud(c_arr, i))

            if c_arr != origin_arr:
                q.append([[item[:] for item in c_arr], cnt+1, mx])
            else:
                answer = max(answer, mx)
            c_arr = [item[:] for item in origin_arr]


if __name__ == "__main__":
    N = int(input())
    answer = -1
    graph = [list(map(int, input().split())) for _ in range(N)]

    bfs(graph)
    print(answer)
