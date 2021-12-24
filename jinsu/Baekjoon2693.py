import sys
T = int(sys.stdin.readline())

for i in range(T):
    case = list(map(int, sys.stdin.readline().split()))
    case.sort()
    print(case[-3])
