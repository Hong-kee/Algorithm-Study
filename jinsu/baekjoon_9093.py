import sys
T = int(sys.stdin.readline())

for i in range(T):
    a = sys.stdin.readline().split()

    for j in a:
       print(j[::-1], end=' ') 
