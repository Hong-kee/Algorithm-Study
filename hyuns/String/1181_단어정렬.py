# n = int(input())
# data = [input() for _ in range(n)]

# data = sorted(list(set(data)), key=len)
# n_data = [[] for _ in range(51)]
# result = []

# for i in range(len(data)):
#     n_data[len(data[i])].append(data[i])

# for i in n_data:
#     if len(i) > 0:
#         i.sort()
#         result.extend(i)

# for res in result:
#     print(res)

n = int(input())
data = [input() for _ in range(n)]

data = list(set(data))
result = []

for word in data:
    result.append((len(word), word))

result.sort()
for len, res in result:
    print(res)