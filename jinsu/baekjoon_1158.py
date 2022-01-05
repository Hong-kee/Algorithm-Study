import sys
n, k = map(int,sys.stdin.readline().split())

q = []
ans = []
cur = 0

for i in range(1, n+1):
    q.append(i)

while (len(ans) != len(q)):
    if k == len(q):
        k = 0
    ans.append(q[k-1:k])
    k += k
    
print(ans)
