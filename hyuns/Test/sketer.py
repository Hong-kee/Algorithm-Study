
# def dfs(answer, box, idx, command, now_red):

#     if idx == len(command):
#         answer.append(now_red)
#         answer = list(set(answer))
#         return
#     b, a  = command[idx]
#     box[b] = list(set(box[b]))

#     if len(box[b]) >= 2:
#         for ball in (1, 0):
#             box[a].append(ball)
#             box[b].remove(ball)
#             if ball == 1:
#                 dfs(answer, box, idx+1, command, a)
#             else:
#                 dfs(answer, box, idx+1, command, now_red)
#             box[a].pop()
#             box[b] = [1, 0]
#     elif len(box[b]) == 1:
#         box[a].append(box[b][0])
#         if box[b].pop() == 1:
#             dfs(answer, box, idx+1, command, a)
#         else:
#             dfs(answer, box, idx+1, command, now_red)
#         box[b].append(box[a].pop())

#     else:
#         dfs(answer, box, idx+1, command, now_red)

#     return

# def solution(N, M, command):
#     answer = []
#     box = [[0] for _ in range(N+1)] # white : 0
#     box[1] = [1] # Red : 1
#     dfs(answer, box, 0, command, 1)

#     return list(set(answer))

# print(solution(4, 4, [[1, 2], [2, 3], [2, 3], [4, 2]]))


# 토너먼트


def decide_graph(day, names, busyness):
    graph = [[] for _ in range(len(names))]
    for player in range(len(names)):
        graph[player] = [busyness[player][day], names[player]]
    
    # 정렬
    graph = sorted(graph)
    draw = []
    for idx in range(0, len(graph), 2):
        draw.append([names.index(graph[idx][1]), names.index(graph[idx+1][1])])
    return draw

def win_condition(player1, player2):
    # c1
    if sum(sorted(player1)[-2:]) > sum(sorted(player2)[-2:]):
        return player1
    elif sum(sorted(player1)[-2:]) < sum(sorted(player2)[-2:]):
        return player2
    
    # c2
    if (max(player1) - min(player1)) < (max(player2) - min(player2)):
        return player1
    elif (max(player1) - min(player1)) > (max(player2) - min(player2)):
        return player2
    
    # c3
    return player1

def competition(day, names, eyes, arms, legs,draw):

    for i in range(len(draw)):
        p1_idx, p2_idx = draw[i]
        player1, player2 = [eyes[p1_idx][day], arms[p1_idx][day], legs[p1_idx][day]], [eyes[p2_idx][day], arms[p2_idx][day], legs[p2_idx][day]]
        if win_condition(player1, player2) == player1:
            draw[i] = names[p1_idx]
        else:
            draw[i] = names[p2_idx]

    return draw

def solution(k, names, eyes, arms, legs, busyness):

    for day in range(k):
        draw = decide_graph(day, names, busyness) # 대진표 설정
        names = competition(day, names, eyes, arms, legs, draw)
    return draw[0]

print(solution(2, ["alice", "bob", "carol", "dave"], [[1, 3], [3, 2], [1, 2], [2, 1]], [[4, 2], [4, 3], [4, 1], [2, 3]], [[1, 5], [3, 2], [3, 4], [1, 2]], [[1, 3], [3, 2], [3, 1], [1, 2]]))