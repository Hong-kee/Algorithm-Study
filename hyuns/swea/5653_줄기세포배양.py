import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def breeding_cell(x, y, status, visit):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for mode in range(4):
        mx, my = x + dx[mode], y + dy[mode]
        if visit[mx][my] == False and status[mx][my] >= 0:

def update_state(state):
    for i in range(M):
        for j in range(N):
            if original_graph[i][j] == 0:
                continue
            elif original_graph[i][j] > 0 and change_graph == 0:




for test_case in range(1, T + 1):
    N, M, K = map(int, input.split())
    original_graph = [list(map(int, input.split())) for _ in range(M)] # 원래 생명력
    change_graph = [item[:] for item in original_graph] # 생명력 변화 표
    state_graph = [[0] * N for _ in range(M)] # 0: 아무것도 아님, 1: 비활성, 2: 활성, -1: 죽음

    update_state(state_graph)
    while K != 0: # change_time
        K -= 1

        for i in range(M):
            for j in range(N):
                if change_graph[i][j] > 1: # 비활성 상태
                    change_graph[i][j] -= 1
                elif change_graph[i][j] == 1:  # 1시간 남았으므로, 번식 상태로 변경
                    change_graph[i][j] = -1
                elif change_graph[i][j] == -1:  # 번식 상태이므로, 죽이고(활성상태) 번식시키기
                    change_graph[i][j] = 0
                    breeding_cell(i, j, change_graph)




