import sys; input = sys.stdin.readline


def rotate_pattern(c, x, y, pattern):

    if c == 1:
        pattern[0] = [pattern[0][-1]] + pattern[0][:-1]
        pattern[1][0], pattern[1][2] = pattern[0][0], pattern[0][2]
    elif c == 2:
        pattern[0] = pattern[0][1:] + [pattern[0][0]]
        pattern[1][0], pattern[1][2] = pattern[0][0], pattern[0][2]
    elif c == 3:
        pattern[1] = pattern[1][1:] + [pattern[1][0]]
        pattern[0][0], pattern[0][2] = pattern[1][0], pattern[1][2]
    elif c == 4:
        pattern[1] = [pattern[1][-1]] + pattern[1][:-1]
        pattern[0][0], pattern[0][2] = pattern[1][0], pattern[1][2]

    if graph[x][y] == 0:
        graph[x][y] = pattern[0][2]
    else:
        pattern[0][2], pattern[1][2] = graph[x][y], graph[x][y]
        graph[x][y] = 0

    return pattern[0][0]


if __name__ == "__main__":
    # sys.stdin = open("14499_test.txt", "r")
    # T = int(input())

    # for test_case in range(1, T + 1):
    N, M, x, y, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    command = list(map(int, input().split()))
    pattern = [[0] * 4 for _ in range(2)] # top -> east, top-> south
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for c in command:
        mx = x + dx[c-1]
        my = y + dy[c-1]

        if 0 <= mx < N and 0 <= my < M:
            print(rotate_pattern(c, mx, my, pattern))
            x, y = mx, my
