N = int(input())
i = 1
while i != (2*N):
    if i <= N:
        print("*"*i + " "*(N-i) + " "*(N-i) + "*"*i)
    else:
        print("*"*(2*N-i) + " "*(i-N) + " "*(i-N) + "*"*(2*N-i))
    i+=1
