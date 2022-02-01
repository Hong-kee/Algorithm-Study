n = int(input())
data = []
number = []
for _ in range(n):
    data.append(list(map(int, input().split())))


for i in range(n):
    cnt = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 브루트포스
            cnt += 1
    number.append(cnt)


for result in number:
    print(result, end=' ')