from copy import deepcopy

def fill_zeroToSee(dir, tmp_graph, x, y):

    for i in dir:
        zeroToSee = 1
        if i == 0:
            while y+zeroToSee != M and tmp_graph[x][y+zeroToSee] != 6:
                tmp_graph[x][y+zeroToSee] = '#'
                zeroToSee += 1
        elif i == 1:
            while (x+zeroToSee) != N and tmp_graph[x+zeroToSee][y] != 6:
                tmp_graph[x+zeroToSee][y] = '#'
                zeroToSee += 1
        elif i == 2:
            while (y-zeroToSee) != -1 and tmp_graph[x][y-zeroToSee] != 6:
                tmp_graph[x][y-zeroToSee] = '#'
                zeroToSee += 1
        else:
            while (x-zeroToSee) != -1 and tmp_graph[x-zeroToSee][y] != 6:
                tmp_graph[x-zeroToSee][y] = '#'
                zeroToSee += 1
    return tmp_graph

def dfs(answer, idx, graph, cctv_location, mode):

    if idx == len(cctv_location):
        return sum([arr.count(0) for arr in graph])

    cctv_num, x, y = cctv_location[idx]

    for dir in mode[cctv_num]:
        tmp_graph = deepcopy(graph)
        tmp_graph = fill_zeroToSee(dir, tmp_graph, x, y)
        answer = min(answer, dfs(answer, idx+1, tmp_graph, cctv_location, mode))
    
    return answer

def main():
    cctv_location = []
    mode = [[], 
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3, 0, 1]],
    [[0,1,2,3]]
    ]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] in [1,2,3,4,5]:
                cctv_location.append([graph[i][j], i,j])

    return dfs(N*M, 0, graph, cctv_location, mode)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(main())