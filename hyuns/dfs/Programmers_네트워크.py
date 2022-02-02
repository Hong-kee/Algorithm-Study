# 2차 풀이 - 실패
def dfs(x, computers, visit):
    for i in range(len(computers)):
        if visit[i] == False and computers[x][i] == 1:
            visit[i] = True
            dfs(i, computers, visit)

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]
    
    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            dfs(i, computers, visit)
            answer += 1

    return answer

print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))



# 1차 풀이
# def dfs(computers, index, visit):
#     for i in range(len(computers[index])):
#         if computers[index][i] == 1 and visit[i] == False:
#             visit[i] = True
#             dfs(computers, i, visit)
#     return None
# def solution(n, computers):
#     answer = 0
#     visit = [False for _ in range(n)]
    
#     for i in range(n):
#         if visit[i] == False:
#             dfs(computers, i, visit)
#             answer += 1
#     return answer

