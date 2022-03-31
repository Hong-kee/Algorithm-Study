# import datetime
# from collections import Counter

# def check_membership(money):
#     if 0 <= money < 10000:
#         return 0
#     elif 10000 <= money <20000:
#         return 1
#     elif 20000 <= money <50000:
#         return 2
#     elif 50000 <= money <100000:
#         return 3
#     else:
#         return 4

# def split_get_days(record):
#     date, money = record.split()
#     y, m, d = map(int, date.split("/"))
#     days = (datetime.datetime(y,m,d) - datetime.datetime(y,1,1)).days
#     return days, int(money)

# def solution(purchase):
#     answer = [0,0,0,0,0]
#     cal = [0] * 365
    
#     # 멤버쉽 기간 때, 금액 넣기
#     for record in purchase:
#         days, money = split_get_days(record)

#         for i in range(30):
#             if days + i == 365:
#                 break
#             cal[days+i] += money


#     for money, day in Counter(cal).items():
#         idx = check_membership(money)
#         answer[idx] += day
    
#     return answer



# # purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
# purchase =["2019/01/02 100000", "2019/04/01 10000", "2019/05/01 20000", "2019/06/01 50000", "2019/07/01 100000"]
# print(solution(purchase))


# Problem 2 n목 두기

def solution(h, w, n, board):
    answer = 0
    graph = []
    for i in board:
        ver = []
        for j in i:
            ver.append(int(j))
        graph.append(ver)
    
    print(graph)
        

    # check vertical
    
    for arr in graph:
        d = {0:0, 1:0}
        for i in arr:
            if i == 0:
                if d[1] == n:
                    answer += 1
                d[1] = 0
            else:
                d[1] += 1
        if d[1] == n:
            answer +=1


    # check heiht


    for idx in range(len(graph[0])):
        if idx >= n:
            k = 0
            d = {0:0, 1:0}
            while idx-k != 0:
                if graph[k][idx-k] == 0:
                    if d[1] == n:
                        answer += 1
                    d[1] = 0
                else:
                    d[1] += 1
                k+=1
            if d[1] == n:
                answer += 1

    # check up to down



    # check down to up

    return answer

# h, w, n, board = 7, 9, 4, ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]
h, w, n, board = 5, 5, 5, ["11111", "11111", "11111", "11111", "11111"]
print(solution(h, w, n, board))

# Problem 3 - 처음 상태로

# def solution(grid):
#     answer = -1
#     return answer


# grid = [[1,1,1,1],[2,1,2,2],[2,2,2,1],[1,1,2,2]]
# print(solution(grid))