

def make_dragon(info):
    x, y, d, g = info
    d_mode = [(1,0), (0,1), (-1,0), (0,-1)]

    if g == 0:
        dx, dy = d_mode[d]
        graph[x][y] = True
        graph[x+dx][y+dy] = True
        return

    store_dir = [d]

    for g_idx in range(g+1):
        if g_idx == 0:
            dx,dy = d_mode[store_dir[-1]]
            graph[x][y] = True
            x, y = x-dx, y-dy
            store_dir.append(d)
            d = d-1 if d-1>=0 else 3
        
        else:
            dx, dy = d_mode[d]
            graph[x][y] = True
            x, y = x+dx, y+dy

            nd = store_dir[-1]
            new_store = [d]
            for sd in store_dir[::-2]:
                
                move_d = sd-nd
                dx, dy = d_mode[move_d] # 이전꺼에서 방향만 가져오기
                x, y = x+dx, y+dy
                graph[x][y] = True
            
            store_dir.extend(new_store)
            d = move_d

def main():

    answer = 0
    mc, mx = 102, -1
    for info in dragon_info:
        make_dragon(info)


    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
                answer += 1

    return answer

if __name__ == "__main__":
    n = int(input())
    dragon_info = [list(map(int, input().split())) for _ in range(n)]
    graph = [[False] * 101 for _ in range(101)]
    main()