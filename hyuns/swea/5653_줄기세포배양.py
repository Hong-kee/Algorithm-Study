import sys
sys.stdin = open("input_5653.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리 합니다.


def stretch_graph(origin, state, change):
    new_originGraph = [[0] * len(origin[0])+2 for _ in range(len(origin)+2)]
    new_stateGraph = [[0] * len(origin[0]) + 2 for _ in range(len(origin) + 2)]
    new_changeGraph = [[0] * len(origin[0]) + 2 for _ in range(len(origin) + 2)]

    for i in range(1, len(new_originGraph)-1):
        for j in range(1, len(new_originGraph[i])-1):
            new_originGraph[i][j] = origin[i-1][j-1]
            new_stateGraph[i][j] = state[i-1][j-1]
            new_changeGraph[i][j] = change[i-1][j-1]

    return new_originGraph, new_stateGraph, new_changeGraph


def breeding_cell(x, y, origin, state, change):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for mode in range(4):
        mx, my = x + dx[mode], y + dy[mode]
        if mx < 0 or mx >= len(origin) or my < 0 or my >= len(origin[0]):
            origin, state, change = stretch_graph(origin, state, change)
        if state_graph[mx][my] == 0:
            change[mx][my] = max(change[mx][my], change[x][y])


def update_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if original_graph[i][j] > 0 and state_graph[i][j] == 0:
                state_graph[i][j] = -1


for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    original_graph = [list(map(int, input().split())) for _ in range(M)]  # 기본 생명력
    change_graph = [item[:] for item in original_graph]  # 생명력 변화 표
    state_graph = [[0] * N for _ in range(M)]  # -1: 비활성, 0: 아무것도 아님 or 번식된 애 or 죽음, 1: 활성

    update_state(state_graph)
    while K != 0:  # change_time
        K -= 1
        breeding_list = []

        for i in range(len(original_graph)):
            for j in range(len(original_graph[i])):
                if change_graph[i][j] >= 1:  # 생명력이 있을 경우,

                    if state_graph[i][j] == 1 and original_graph[i][j] == change_graph[i][j]:  # 활성이고 생명력 그래프와 같을 경우,
                        breeding_cell(i, j, original_graph, state_graph, change_graph)  # 번식, 생명력 비교 후, change_graph 변화
                    elif state_graph[i][j] != 0:
                        change_graph[i][j] -= 1  # 생명력 감소

                elif change_graph[i][j] == 0:  # 생명력이 없을 경우,

                    if state_graph[i][j] == -1:  # 비활성 경우
                        change_graph[i][j] = original_graph[i][j]  # 생명력 복귀
                        state_graph[i][j] = 1
                    elif state_graph[i][j] == 1:  # 활성 경우
                        change_graph[i][j] = -1
                        state_graph[i][j] = 0

        original_graph = [item[:] for item in change_graph]  # 생명력 변화 표
        update_state(state_graph)

    sum_state = 0
    for i in range(len(state_graph)):
        for j in range(len(state_graph[0])):
            if state_graph[i][j] == 1 or state_graph[i][j] == -1:
                sum_state += 1
    print(f"# {sum_state}")