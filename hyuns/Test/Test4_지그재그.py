'''

n, r, c가 주어질 때, 그래프는 다음과 같이 지그재그 순으로 그려진다. 

n = 5 일 때, r = 5, c = 2라면 19 를 리턴

1  2  6  7  15 
3  5  8  14 16
4  9  13 17 22
10 12 18 21 23
11 19 20 24 25

n = 6 일 때, r = 5, c = 4라면, 29를 리턴

1  2  6  7  15 16 
3  5  8  14 17 26
4  9  13 18 25 27
10 12 19 24 28 33
11 20 23 29 32 34
21 22 30 31 35 36

알고리즘 ㄱㄱ

'''

# 풀이 1

def solution(n, r, c):
    
    graph = [[0] * n for _ in range(n)]

    start = 0
    # 오른 위로, 왼 아래로
    # 시작과 끝 파악, 중간에 어떻게 계산되는지 파악
    dir = True
    for i in range(2*n-1):

        if i < n:
            if dir:
                for j in range(i+1):
                    start += 1
                    graph[i-j][j]=start
                    
            else:
                for j in range(i+1):
                    start += 1
                    graph[j][i-j]=start
        else:
            if dir:
                for j in range(n-1, i-n, -1):
                    start += 1
                    graph[j][i-j]=start
                    
            else:
                for j in range(n-1, i-n, -1):
                    start += 1
                    graph[i-j][j]=start
                
        dir = not dir

    return graph[r-1][c-1]

print(solution(6, 3, 2))
    

