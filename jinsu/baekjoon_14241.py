import sys
cnt = int(sys.stdin.readline())
seul = list(map(int, sys.stdin.readline().split()))

score = []
result = 0

while len(seul) != 1:
    seul.sort()
    seul.append(seul[0]+seul[1])        # seul = [1,2,3,3] / seul = [3,3,6]
    score.append(seul[0]*seul[1])       # score = [2] / score = [2,9]
    del seul[0]                         # seul = [2,3,3] / seul = [3,6]
    del seul[0]                         # seul = [3,3] / seul = [6]
    

for i in score:
    result += i

print(result)


