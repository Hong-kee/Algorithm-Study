from collections import deque
def solution(n, edge):
    answer = 0
    route = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    q = deque()
    q.append(1)
    route[1] = 1
    while q:
        r = q.popleft()
        for i in graph[r]:
            if route[i] == 0:
                route[i] = route[r] + 1
                q.append(i)
                
    for idx in range(len(route)):
        if route[idx] == max(route):
            answer += 1

    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n, edge))