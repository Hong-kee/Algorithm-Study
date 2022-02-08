# Prime Number
from math import sqrt

# Sol1. - PrimeNum 판별
def PrimeNum(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

# Sol2. - 범위 내, Prime 다 찾기
def eratosSeive(n):
    data = [True] * (n+1)
    for i in range(2, n+1):
        if data[i] == True:
            for j in range(i+i, n+1, i):
                data[j] = False
    
    ans = []
    for i in range(1, len(data)):
        if data[i] == True:
            ans.append(i)
    return ans

if __name__ == "__main__":
    print(PrimeNum(25))
    print(eratosSeive(25))