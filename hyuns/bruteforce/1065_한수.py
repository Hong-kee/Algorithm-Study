n = int(input())
data = []
ans = 0
for i in range(1, n+1):
    diff = int(str(i)[0])
    flag = True

    if len(str(i)) >= 3:

        diff = int(str(i)[1]) - int(str(i)[0])

        for j in range(2, len(str(i))):
            if j * diff != (int(str(i)[j]) - int(str(i)[0])):
                flag = False
                break

    if flag:
        ans += 1
    
print(ans)