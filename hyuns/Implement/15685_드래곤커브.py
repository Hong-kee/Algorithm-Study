
def count_square(answer, graph):

    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
                answer += 1

    return answer

def make_direction(info):
    x, y, d, gen = info
    direct = [d]

    for g in range(1, gen+1):
        new_list = []
        for direct_d in direct[::-1]:
            direct_d = direct_d+1 if direct_d+1 <= 3 else 0
            new_list.append(direct_d)
        direct = direct + new_list
    return direct

def make_dragon(direction, info):
    x, y, d, gen = info
    graph[y][x] = True

    for i in direction:
        y, x = y+dy[i], x+dx[i]
        if 0 <= y <= 100 and 0 <= x <= 100:
            graph[y][x] = True

if __name__ == "__main__":
    n = int(input())
    dragon_info = [list(map(int, input().split())) for _ in range(n)]
    graph = [[False] * 101 for _ in range(101)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    answer = 0
    dragon_direction = []

    for info in dragon_info: # 방향 그려주기
        dragon_direction.append(make_direction(info))
    
    for idx in range(len(dragon_direction)): # 점 찍기 (선 그리기)
        make_dragon(dragon_direction[idx], dragon_info[idx])

    answer = count_square(answer, graph) # 사각형 개수 세기
    
    print(answer)