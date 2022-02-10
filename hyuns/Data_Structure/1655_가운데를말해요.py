# 정수를 하나씩 외칠때마다 말한 수 중에서 중간값
# 짝수개라면, 중간값들 중 작은값

# sol1
# 중간값을 기준으로 작은 수들의 우선순위 큐, 큰 수들의 우선 순위 큐에 넣기
# 중간값은 두 개의 큐의 가장 위에 있는 수를 비교해서 가져오기

import sys
import heapq as hq

N = int(sys.stdin.readline())
mid = int(sys.stdin.readline())
min_q, max_q, answer = [], [], [mid]

for i in range(1, N):
    numb = int(sys.stdin.readline())
    mins, maxs = min(mid,numb), max(mid,numb)
    hq.heappush(min_q, (-mins, mins))
    hq.heappush(max_q, (maxs, maxs))
    
    if len(min_q) >= len(max_q):
        mid = hq.heappop(min_q)[1]
    else:
        mid = hq.heappop(max_q)[1]
    
    answer.append(mid)

for i in answer:
    print(i)