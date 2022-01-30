s1 = input()
s2 = input()
answer = 0
graph = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1] == s2[i-1]:
            graph[i][j] = graph[i-1][j-1] + 1
            answer = max(graph[i][j], answer)

print(answer)