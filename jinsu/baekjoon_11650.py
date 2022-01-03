import sys
number = int(sys.stdin.readline())
location = []
for _ in range(number):
    x, y = map(int, sys.stdin.readline().split())
    location.append([x, y])

location.sort(key=lambda x: x[1])
location.sort(key=lambda x: x[0])


for i in range(len(location)):
    print(location[i][0],location[i][1])
