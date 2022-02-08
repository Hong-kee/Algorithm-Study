from math import sqrt
def isPrimeNum(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

n, cnt = int(input()), 0
data = list(map(int, input().split()))

for i in data:
    if i!=1 and isPrimeNum(i): cnt+=1

print(cnt)