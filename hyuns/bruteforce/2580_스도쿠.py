data_x, data_y, data_m = [], [], []
zero_x, zero_y, zero_m = [], [], []

# for i in range(9):
#     data.append(list(map(int, input().split())))

for i in range(9):
    data = list(map(int, input().split()))
    zero = 0
    for j in data:
        if j == 0:
            zero += 1
    data_x.append(data)
    zero_x.append(zero)

for i in range(9):
    data = []
    zero = 0
    for j in range(9):
        data.append(data_x[j][i])
        if data_x[j][i] == 0:
            zero += 1
    data_y.append(data)
    zero_y.append(zero)

data_m = [[] for _ in range(9)]
for i in range(0, 9, 3):
    for j in range(3):
        data_m[i].extend(data_x[j][:3])
        data_m[i+1].extend(data_x[j][3:6])
        data_m[i+2].extend(data_x[j][6:])
        





# for x in range(len(data)):
#     ch = [1,2,3,4,5,6,7,8,9]
#     flag = []

#     for i in range(len(data[x])):
#         data_y.append()

#         if data[x][i] == 0:
#             flag.append(data[x])
#             continue
#         ch.remove(x[i])

#     if len(ch) == 1: # 1개만 있는 애들 채워주기
#         data[x][flag[0]] = ch[0]


# def dfs(data, )
# for i in range(9):
#     for j in range(9):
#         dfs(data, [])




# 백트래킹 이용
# 가로, 세로, 정사각형 조건 확인
# 점검 (가로, 세로, 가운데 점검)
# 1. 숫자가 남은 하나라면, 숫자 바꾸기 
# 2. 0이 하나 더 있다면 들어가기 -> 다음 점검은 가로부터
# 각 박스마다 num의 개수를 따져서 적은 곳부터 들어가기


# for i in range()