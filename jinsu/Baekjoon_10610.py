n = list(input())
n.sort(reverse=True)
answer = -1

print(n)
n = int(''.join(n))
print(n)

if n % 30 == 0:
    answer = n

print(answer)




