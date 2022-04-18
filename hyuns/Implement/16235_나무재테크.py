import sys
input = sys.stdin.readline

#
# sys.stdin = open("input_16234.txt", "r")
#
# T = int(input())


def spring(feedState, tree):
    dead_tree = []

    for i in range(N):
        for j in range(N):
            new_tree = []
            for z in sorted(tree[i][j]):
                if feedState[i][j] >= z:
                    feedState[i][j] -= z
                    new_tree.append(z + 1)
                else:
                    dead_tree.append([i, j, z])
            tree[i][j] = new_tree

    return dead_tree


def summer(feedState):
    for x, y, z in deadTree_info:
        feedState[x][y] += z // 2


def fall(tree):
    for x in range(N):
        for y in range(N):
            for z in tree[x][y]:
                if z % 5 == 0:
                    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                        mx, my = x + dx, y + dy
                        if 0 <= mx < N and 0 <= my < N:
                            tree[mx][my].append(1)


def winter(feedState):
    for i in range(len(feed)):
        for j in range(len(feed[i])):
            feedState[i][j] += feed[i][j]


def make_treeGraph(tree):
    tree_graph = [[[] for _ in range(N)] for _ in range(N)]
    for x, y, z in tree:
        tree_graph[x - 1][y - 1].append(z)
    return tree_graph



# for test_case in range(1, T + 1):

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    feed = [list(map(int, input().split())) for _ in range(N)]
    tree_info = [list(map(int, input().split())) for _ in range(M)]
    tree_info = make_treeGraph(tree_info)
    cur_feedState = [[5] * N for _ in range(N)]

    for _ in range(K):
        deadTree_info = spring(cur_feedState, tree_info)
        summer(cur_feedState)
        fall(tree_info)
        winter(cur_feedState)

    answer = 0
    for i in range(len(tree_info)):
        for j in range(len(tree_info)):
            if tree_info[i][j]:
                answer += len(tree_info[i][j])
    print(answer)
