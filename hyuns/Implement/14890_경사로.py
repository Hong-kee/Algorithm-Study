N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visit_r = [[False] * N for _ in range(N)]
visit_c = [[False] * N for _ in range(N)]

def check_left_slope(x, y, row):
    if row:
        for i in range(1, L+1):
            if (y-i) < 0:
                return False
            if visit_r[x][y-i] == True or graph[x][y] - graph[x][y-i] != 1:
                return False
            visit_r[x][y-i] = True
    else:
        for i in range(1, L+1):
            if (x-i) < 0:
                return False
            if visit_c[x-i][y] == True or graph[x][y] - graph[x-i][y] != 1:
                return False
            visit_c[x-i][y] = True
    return True

def check_right_slope(x, y, row):
    if row:
        for i in range(1, L+1):
            if (y+i) >= N:
                return False
            if visit_r[x][y+i] == True or graph[x][y] - graph[x][y+i] != 1:
                return False
            visit_r[x][y+i] = True
    else:
        for i in range(1, L+1):
            if (x+i) >= N:
                return False
            if visit_c[x+i][y] == True or graph[x][y] - graph[x+i][y] != 1:
                return False
            visit_c[x+i][y] = True
    return True

def check_graph(x, y, row):

    if row:
        while y < N-1:
            
            if graph[x][y] - graph[x][y+1] == 0:
                y += 1
                continue
            elif graph[x][y] - graph[x][y+1] == 1:
                if check_right_slope(x, y, row):
                    y += L
                    continue
            elif graph[x][y] - graph[x][y+1] == -1:
                if check_left_slope(x, y+1, row):
                    y += 1
                    continue
            return 0
    else:
        while x < N-1:
            
            if graph[x][y] - graph[x+1][y] == 0:
                x += 1
                continue
            elif graph[x][y] - graph[x+1][y] == 1:
                if check_right_slope(x, y, row):
                    x += L
                    continue
            elif graph[x][y] - graph[x+1][y] == -1:
                if check_left_slope(x+1, y, row):
                    x += 1
                    continue

            return 0
    return 1

ans = 0
for i in range(N):
    ans += check_graph(i, 0, True) + check_graph(0, i, False)
print(ans)