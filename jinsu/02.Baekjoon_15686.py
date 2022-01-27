from itertools import combinations
N, M = map(int, input().split())
data = [] # 도시의 정보 저장할 리스트
chicken = [] # 치킨 가게 좌표 저장할 리스트
home = [] # 집 좌표 저장할 리스트

for _ in range(N):
    data.append(list(map(int, input().split())))

for chicken_x in range(N):
    for chicken_y in range(N):
        if data[chicken_x][chicken_y] == 2:
            chicken.append((chicken_x+1, chicken_y+1))

for home_x in range(N):
    for home_y in range(N):
        if data[home_x][home_y] == 1:
            home.append((home_x+1, home_y+1))

temp = 10000
for ch in combinations(chicken, M): # 조합을 이용하는 것이 포인트
    sum = 0
    for h in home:
        sum += min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in ch]) # 중요 포인트
        if sum >= temp:
            break
    if sum < temp:
        temp = sum
print(temp)



    


    
