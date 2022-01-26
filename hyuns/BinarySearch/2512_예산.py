n = int(input())
data = list(map(int, input().split()))
m = int(input())
data.sort()

if sum(data) <= m: # 모두 합했을 때, 예산보다 적은 경우
    print(max(data))

elif min(data) * n > m: # 가장 최소의 예산으로 이루어졌을 때, 예산이 적은 경우
    min, max = 1, min(data)
    result = 0
    while True:
        mid = (min + max) // 2
        
        if mid * n == m or min == mid:
            result = mid
            break
        elif mid * n > m:
            max = mid
        else:
            min = mid
    print(result)

else: # 최소 예산 이상 최대 예산 이하로 만들 수 있을 때, 예산이 많은 경우
    min, max = data[0], data[-1]
    result = 0
    while True:
        mid = (min + max) // 2
        ans = 0
        for i in data:
            if i <= mid:
                ans += i
            else:
                ans += mid
        
        if ans == m or min == mid:
            result = mid
            break

        elif ans > m:
            max = mid
        else:
            min = mid
    
    print(result)