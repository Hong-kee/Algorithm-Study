import sys
T = int(sys.stdin.readline())


for _ in range(T):
    subs = []
    tree_cnt = int(sys.stdin.readline())
    tree_height = list(map(int, sys.stdin.readline().split()))

    tree_height.sort(reverse=True)

    for i in range(1, len(tree_height)):
        subs.append(tree_height[0] - tree_height[i])
    subs.sort()
    print(subs[1])

