import sys
from collections import deque
input = sys.stdin.readline


def change_direction(sn_info, direction):
    _, after_direction = sn_info.popleft()
    direction = direction + 1 if after_direction == "D" else direction - 1

    if direction == 4:
        direction = 0
    elif direction == -1:
        direction = 3

    return direction


def start(arr, sn_info):
    time = 0
    sn_x, sn_y = 0, 0
    arr[sn_x][sn_y] = 9
    snake = deque()
    snake.append([sn_x, sn_y])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0  # 오른쪽

    while True:
        time += 1
        sn_x += dx[d]
        sn_y += dy[d]
        if 0 <= sn_x < N and 0 <= sn_y < N:
            if arr[sn_x][sn_y] == 1:
                snake.append([sn_x, sn_y])
                arr[sn_x][sn_y] = 9
            elif arr[sn_x][sn_y] == 9:
                break
            else:
                sn_tail_x, sn_tail_y = snake.popleft()
                snake.append([sn_x, sn_y])
                arr[sn_tail_x][sn_tail_y] = 0
                arr[sn_x][sn_y] = 9
        else:
            break

        if sn_info and sn_info[0][0] == time:
            d = change_direction(sn_info, d)

    return time


if __name__ == "__main__":
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1

    L = int(input())
    snake_info = deque()
    for _ in range(L):
        t, d = input().split()
        snake_info.append([int(t), d])

    print(start(graph, snake_info))
