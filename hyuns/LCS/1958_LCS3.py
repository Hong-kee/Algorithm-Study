
# 풀이
'''
고민하다가 도저히 2차원은 안될거 같아서, 풀이를 보고 3차원이 해답이라는 것을 알았다.

3차원의 힌트를 얻고 2차원과 같은 조건으로 LCS를 구했다.
'''
s1, s2, s3 = input(), input(), input()
answer = 0

graph = [[[0] * (len(s1)+1) for _ in range(len(s2)+1)] for _ in range(len(s3)+1)]

for i in range(1, len(s3)+1):
    for j in range(1, len(s2)+1):
        for k in range(1, len(s1)+1):
            if s1[k-1] ==  s2[j-1] == s3[i-1]:
                graph[i][j][k] = graph[i-1][j-1][k-1] + 1
                answer = max(answer, graph[i][j][k])
            else:
                graph[i][j][k] = max(graph[i-1][j][k], graph[i][j-1][k], graph[i][j][k-1], graph[i-1][j-1][k], graph[i-1][j][k-1], graph[i][j-1][k-1])
print(answer)

# 틀린 풀이
'''
s1, s2의 공통 부분 문자열(s4)을 모두 구한 후, 
s3, s4의 LCS를 구한다. 

결과, 메모리 초과가 떴다..ㅠ
'''
# s1, s2, s3 = input(),input(),input()

# # s1, s2의 공통 부분 문자열 구하기

# n, m = len(s1), len(s2)
# graph = [[0] * (n+1) for _ in range(m+1)]
# result= [""]


## def find_sub(graph, m, n):
##     global ans, result
##     if graph[m][n] == 0:
##         result.append(ans[::-1])
##         ans = ""
##         return
#
##     if graph[m][n] == graph[m-1][n]:
##         find_sub(graph, m-1, n)
##     if graph[m][n] == graph[m][n-1]:
##         find_sub(graph, m, n-1)
##     if graph[m][n] != graph[m][n-1] and graph[m][n] != graph[m-1][n]:
##         ans += s2[m-1]
##         find_sub(graph, m-1, n-1)

# for i in range(1,(m+1)):
#     for j in range(1, (n+1)):
#         if s1[j-1] == s2[i-1]:
#             graph[i][j] = graph[i-1][j-1] + 1

#             if graph[i][j] == len(result[0]):
#                 ans = result[0][:-1] + s1[j-1]
#                 result.append(ans)
#             else:
#                 result[0] = result[0] + s1[j-1]
            
#         else:
#             graph[i][j] = max(graph[i-1][j], graph[i][j-1])

## find_sub(graph, m, n)
# # s3, s4의 공통 부분 문자열 길이 구하기
# answer = 0
# for s4 in result:
#     n, m = len(s3), len(s4)
#     graph = [[0] * (n+1) for _ in range(m+1)]

#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s3[j-1] == s4[i-1]:
#                 graph[i][j] = graph[i-1][j-1] +1
#                 answer = max(answer, graph[i][j])
#             else:
#                 graph[i][j] = max(graph[i-1][j], graph[i][j-1])

# print(answer)

