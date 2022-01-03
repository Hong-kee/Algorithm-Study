import sys
N = int(sys.stdin.readline())
q = []

for i in range(N):
    cm = sys.stdin.readline().split()

    if (cm[0] == 'push'):
        q.append(cm[1])

    elif cm[0] == 'pop':
        if not q:
            print(-1)
        else:
            p = q.pop(0)
            print(p)
    elif cm[0] == 'size':
        print(len(q))
    
    elif cm[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif cm[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    
    elif cm[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
