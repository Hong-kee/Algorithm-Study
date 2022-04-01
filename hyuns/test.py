def test():
    graph[0] = max(graph[0], C)
    return max(graph[0], C)


a, b = 1, 2
for i in range(2):
    answer = -1
    C = 3
    graph = [1, 2, 3]
    print(test())
    print(C)

print(answer)
