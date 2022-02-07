from selectors import SelectSelector


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def select_dir(d):
    
    if d == 0:
        return (0,-1), (1,0), (0,1), (-1,0)
    elif d == 1:
        return (-1,0), (0,-1), (1,0), (0,1)
    elif d == 2:
        return (0,1), (-1,0), (0,-1), (1,0)
    else:
        return (1,0), (0,1), (-1,0), (0,-1)

def clean_cur(graph, x, y):
    graph[x][y] = 2
    return 1

def turn_dir(d):
    d -= 1
    if d == -1:
        return 3
    return d

def bfs(x,y,d):
    
    global graph   
    answer = 0
    '''
    1. 현재 위치 청소
    2. 현재 방향을 기준으로 왼쪽부터 탐색
    왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    '''

    # clean cur
    answer += clean_cur(graph, x, y)
    # Search
    while True:
        flag = True
        md = d
        for dx, dy in select_dir(d):
            mx, my = x+dx, y+dy
            if graph[mx][my] == 1 or graph[mx][my] == 2:
                md = turn_dir(md)
                continue
            if graph[mx][my] == 0:
                md = turn_dir(md)
                x, y = mx, my
                answer += clean_cur(graph, x, y)
                flag=False
                break
        
        if flag:
            dx, dy = select_dir(md)[1]
            mx, my = x+dx, y+dy
            if graph[mx][my] == 1:
                break
            else:
                x, y = mx, my
        d = md

    return answer

answer = bfs(r,c,d)
print(answer)