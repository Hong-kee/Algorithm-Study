# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# ans = 0
# for i, (n, w) in enumerate(data):

#     sort_data = sorted(data[i+1:], key=lambda x:(x[1],x[0]))

#     for ii, (nn, ww) in enumerate(sort_data):

#         nn, ww = sort_data[ii]
        
#         f_n = n - ww
#         s_n = nn - w

#         # 둘 다 안깨질 경우
#         while (f_n >= 0 and nn >= 0):
#             n -= ww # 치는 계란 깨기
#             nn -= w # 맞는 계란 꺠기

#         if n < 0 and nn < 0: # 둘다 깨질 경우
#             # check.append([nn, ww])
#             data.remove([])
#             ans += 2
#             break
#         elif n < 0: # 하나만 깨질 경우 - 깨는애
#             data[i] = [n, w]
#             ans += 1
#             break
#         elif nn < 0: # 하나만 깨질 경우 - 맞는애\
#             ans += 1
#             ii += 1
#             continue

# print(ans)

## 이해가 안감.. 
# bfs + dfs

# n = int(input())
# egg = [list(map(int, input().split())) for _ in range(n)]
# answer = 0

# def dfs(n_egg, idx, answer):
#     at_x,at_y = n_egg[idx]
#     if at_y < 0:
#         dfs(n_egg, idx+1, answer)
#         return
#     if idx > n:
#         return
    
#     for ii in range(len(n_egg)): # 모든 경우의 수 검사
#         de_x, de_y = n_egg[ii]
#         de_y -= at_x
#         at_y -= de_x

#         if de_x == at_x and de_y == at_y: continue # 현재 값
#         if at_y <= 0:
#             answer += 1
#             n_egg[idx] = [at_x, at_y]
#             n_egg[ii] = [de_x, de_y]
#             dfs(n_egg, idx+1, answer)
#             continue  # 들고 있는게 깨지면 다음꺼
#         if after_at_y <= 0: # 
#             answer+=1
#             n_egg[idx] = [after_at_y, after_de_y]



        



ans = dfs(egg, 0, answer)