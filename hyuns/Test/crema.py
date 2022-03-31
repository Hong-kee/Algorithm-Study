from collections import deque
def bfs(grid1, grid2, visit, i,j):
    
    visit[i][j] = True
    q = deque()
    q.append([i,j])
    answer = 1
    while q:
        x, y = q.popleft()
        if grid1[x][y] != grid2[x][y]:
            answer = 0
    
        for (i, j) in (0,1), (1,0), (0, -1), (-1, 0):
            mx, my = x+i, y+j
            if 0<= mx < len(grid1) and 0<= my < len(grid1):
                if grid1[mx][my] == 1 or grid2[mx][my] == 1:
                    if visit[mx][my] == False:
                        visit[mx][my] = True
                        q.append([mx,my])
    return answer
    
def countMatches(grid1, grid2):
    # Write your code here
    grid1 = [list(map(int, string)) for string in grid1]
    grid2 = [list(map(int, string)) for string in grid2]
    visit = [[False] * len(grid1) for _ in range(len(grid1))]
    answer = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] == 1 and visit[i][j] == False:
                answer += bfs(grid1, grid2, visit, i,j)

    return answer
    

grid1 = [[0,0,1],[0,1,1],[1,0,0]]
grid2 = [[0,0,1],[0,1,1],[1,0,1]]
print(countMatches(grid1, grid2))