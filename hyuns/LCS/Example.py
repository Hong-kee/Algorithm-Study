
'''
1. Longest Common String : 최장 연속 공통 문자열

"GBCDFE" , "ABCDEF" => "BCD"

2. Longest Common Subsequence : 최장 연속 공통 부분 수열

"GBCDFE" , "ABCDEF" => "BCDE" or "BCDF"

'''

# 1번

# s1, s2 = input().split()
# n = len(s1) + 1
# graph = [[0] * n for _ in range(n)]
# answer = 0
# answer2 = []

# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1[i] == s2[j]:
#             graph[i+1][j+1] = graph[i][j] + 1
#             answer = max(answer, graph[i+1][j+1])

# data = ""
# for i in range(len(s1), 0, -1):
#     if graph[i][i] > 0:
#         data = data + s1[i-1]
#     else:
#         if len(data) != 0:
#             answer2.append(data)
#             data = ""

# print(answer)
# print(answer2[0][::-1])

# 2번
# s1, s2 = input().split()
# n = len(s1) + 1
# graph = [[0] * n for _ in range(n)]
# answer, answer2 = 0, ""

# for i in range(1, n):
#     for j in range(1, n):
#         if s1[i-1] == s2[j-1]:
#             graph[i][j] = graph[i-1][j-1] + 1
#             answer = max(answer, graph[i][j])
#         else:
#             graph[i][j] = max(graph[i-1][j], graph[i][j-1])
        
# x, y = n-1, n-1
# while len(answer2) != answer:
#     if graph[x][y] == graph[x-1][y]:
#         x, y = x-1, y
#     elif graph[x][y] == graph[x][y-1]:
#         x, y = x, y-1
#     else:
#         answer2 += s1[x-1]
#         x, y = x-1, y-1
    
# print(answer)
# print(answer2[::-1])