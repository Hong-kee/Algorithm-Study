n = int(input())
data = list(map(int, input().split()))
dp = [n+1] * (n+1)
dp[0] = 0

for now_idx in range(len(data)):
    jump_idx = data[now_idx]

    for ji in range(1, jump_idx+1):
        next_idx = now_idx + ji
        if next_idx >= n:
            break

        dp[next_idx] = min(dp[next_idx], dp[now_idx]+1)

if dp[n-1] == n+1:
    print(-1)
else:
    print(dp[n-1])


# from collections import deque
# n = int(input())
# data = list(map(int, input().split()))

# def search(data, idx):

#     answer = n+1 # 최대 갈 수 있는 값 지정
#     q = deque()
#     q.append([idx, 0])
#     while q:
        
#         idx, ans = q.popleft()

#         for i in range(1, data[idx]+1):
#             if (idx + i) == n: answer = min(ans+1, answer); break   # 정답 idx일 경우, return
#             if (idx + i) >= n: break                                # 정답 idx를 넘을 경우, break
#             if [(idx + i), ans+1] in q: continue                    # 이미 값이 있을 경우, continue
#             if data[idx+i] == 0: continue                           

#             q.append([(idx + i), ans+1])                            # 아니면 collect
    
#     return answer

# answer = search(data, 0)
# if answer <= n-1: print(answer)
# else: print(-1)


# 틀린 답
# n = int(input())
# data = list(map(int, input().split()))
# dp = [0] * (n+1)

# for now_idx in range(len(data)):
#     jump_idx = data[now_idx]

#     for ji in range(1, jump_idx+1):
#         next_idx = now_idx + ji
#         if next_idx >= n:
#             break

#         if dp[next_idx] != 0:
#             dp[next_idx] = min(dp[next_idx], dp[now_idx]+1)
#         else:
#             dp[next_idx] = dp[now_idx]+1

# if dp[n-1] == 0:
#     print(-1)
# else:
#     print(dp[n-1])


n = int(input())
data = list(map(int, input().split()))
dp = [n+1] * (n+1)
dp[0] = 0

for now_idx in range(len(data)):
    jump_idx = data[now_idx]

    for ji in range(1, jump_idx+1):
        next_idx = now_idx + ji
        if next_idx >= n:
            break

        dp[next_idx] = min(dp[next_idx], dp[now_idx]+1)

if dp[n-1] == n+1:
    print(-1)
else:
    print(dp[n-1])