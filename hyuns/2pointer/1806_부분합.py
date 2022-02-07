n, s = map(int, input().split())
data = list(map(int, input().split()))
res = sum(data)
start, end, data_sum = 0, 0, 0
if s <= res:
    while True:

        
        if data_sum >= s:
            res = min(res, end-start)
            data_sum -= data[start]
            start += 1

        elif end == len(data):
            break

        elif data_sum < s:
            data_sum += data[end]
            end += 1

    print(res)
else:
    print(0)