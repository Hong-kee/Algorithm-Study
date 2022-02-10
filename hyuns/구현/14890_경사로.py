# N, L = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# def check_graph(x, y, row):

#     if row:
#         now = graph[x][y]
#         for i in range(1, N):
#             if graph[x][y+i] - now == 0:
#                 continue
#             elif abs(graph[x][y+i] - now) > 1:
#                 print(row, x, y, "False")
#                 return 0

#             now, leng = graph[x][y+i], 0
            
#             for j in range(1, L+1):
#                 if y+i-j < 0:
#                     break
#                 if now - graph[x][y+i-j] == 1:
#                     leng += 1
#                 elif now - graph[x][y+i-j] == -1:
#                     leng -= 1
            
#             if abs(leng) != L:
#                 print(row, x, y, "False")
#                 return 0

#             leng = 0
#             for j in range(1, L+1):
#                 if y+i+j == N:
#                     break
#                 if now - graph[x][y+i+j] == 1:
#                     leng += 1
#                 elif now - graph[x][y+i+j] == -1:
#                     leng -= 1

#             if abs(leng) != L:
#                 print(row, x, y, "False")
#                 return 0

#     else:
#         now = graph[x][y]
#         for i in range(1, N):
#             if graph[x+i][y] - now == 0:
#                 continue
#             elif abs(graph[x+i][y] - now) > 1:
#                 print(row, x, y, "False")
#                 return 0

#             now, leng = graph[x+i][y], 0
            
#             for j in range(1, L+1):
#                 if x+i-j < 0:
#                     break
#                 if now - graph[x+i-j][y] == 1:
#                     leng += 1
#                 elif now - graph[x+i-j][y] == -1:
#                     leng -= 1
            
#             if abs(leng) != L:
#                 print(row, x, y, "False")
#                 return 0

#             leng = 0
#             for j in range(1, L+1):
#                 if y+i+j == N:
#                     break
#                 if now - graph[x+i+j][y] == 1:
#                     leng += 1
#                 elif now - graph[x+i+j][y] == -1:
#                     leng -= 1

#             if abs(leng) != L:
#                 print(row, x, y, "False")
#                 return 0

#     print(row, x, y, "True")
#     return 1

# ans = 0
# for i in range(N):
#     ans += check_graph(i, 0, True) + check_graph(0, i, False)
# print(ans)