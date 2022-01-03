import sys
T = int(sys.stdin.readline())
for i in range(T):
    count = 0
    V = sys.stdin.readline()
    VF = list(V.strip())

    for j in VF:
        if j == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print("NO")
            break
    if count == 0:
        print("YES")
    elif count > 0:
        print("NO")


