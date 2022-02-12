gear = [input() for _ in range(4)]
k = int(input())
move = [list(map(int, input().split())) for _ in range(k)]

def sum_score():
    return sum(2**i if gear[i][0] == '1' else 0 for i in range(4))

def rotate_gear(g_num,dir):
    if dir == -1:
        gear[g_num] = gear[g_num][1:] + gear[g_num][0]
    else:
        gear[g_num] = gear[g_num][-1] + gear[g_num][:-1]

def state_gear(g_num, dir):

    if g_num == 0:
        if not visit[1] and gear[0][2] != gear[1][-2]:
            visit[1] = -dir
            state_gear(1, -dir)
    elif g_num == 1:
        if not visit[0] and gear[0][2] != gear[1][-2]:
            visit[0] = -dir
            state_gear(0, -dir)
        if not visit[2] and gear[1][2] != gear[2][-2]:
            visit[2] = -dir
            state_gear(2, -dir)
    elif g_num == 2:
        if not visit[1] and gear[1][2] != gear[2][-2]:
            visit[1] = -dir
            state_gear(1, -dir)
        if not visit[3] and gear[2][2] != gear[3][-2]:
            visit[3] = -dir
            state_gear(3, -dir)
    else:
        if not visit[2] and gear[2][2] != gear[3][-2]:
            visit[2] = -dir
            state_gear(2, -dir)

for g_num, dir in move:

    visit = [0] * 4
    visit[g_num-1] = dir
    state_gear(g_num-1, dir)

    for i in range(len(visit)):
        if visit[i] != 0: rotate_gear(i, visit[i])

print(sum_score())