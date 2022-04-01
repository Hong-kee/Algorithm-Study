import sys
from collections import deque

sys.stdin = open("input_5656.txt", "r")
T = int(input())


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def destroy_bricks(y, x, destroy_graph):  # bfs 부분에서 계속 삐걱임
    erase_brick = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append([x, y])
    while q:
        nx, ny = q.popleft()
        len_destroy = destroy_graph[nx][ny]
        if len_destroy >= 1:
            destroy_graph[nx][ny] = 0
            erase_brick += 1
            for dl in range(1, len_destroy):
                for d in range(4):
                    mx = nx + dx[d] * dl
                    my = ny + dy[d] * dl
                    if 0 <= mx < H and 0 <= my < W and destroy_graph[mx][my] > 0:
                        q.append([mx, my])

    return erase_brick


def setting_bricks(bricks):
    for w in range(W):
        new = []
        for h in range(H):
            if bricks[h][w] >= 1:
                new.append(bricks[h][w])
                bricks[h][w] = 0

        for nh in range(H - len(new), H):  # out of index 조심
            bricks[nh][w] = new[nh - (H - len(new))]


def dfs(bricks, b_eraseBricks, shooting_cnt):
    global glob_eraseBricks
    if shooting_cnt == 0:
        glob_eraseBricks = max(glob_eraseBricks, b_eraseBricks)
        return
    for w in range(W):
        for h in range(H):
            if bricks[h][w] >= 1:
                break

        origin_bricks = [item[:] for item in bricks]  # deepcopy
        eraseBricks = destroy_bricks(w, h, bricks) # count erase bricks
        setting_bricks(bricks)  # setting
        dfs(bricks, eraseBricks+b_eraseBricks, shooting_cnt - 1) # 이전 erase bricks 추가해서 개수 넣기
        bricks = origin_bricks # copy 후, origin 복귀

    return


for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    glob_eraseBricks = -1

    # 전체 brick 개수 지정
    all_bricks = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] >= 1:
                all_bricks += 1

    dfs(graph, 0, N)

    print(f"#{test_case} {all_bricks - glob_eraseBricks}")
