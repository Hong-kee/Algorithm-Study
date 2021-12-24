import sys
n , m = map(int, sys.stdin.readline().split())
mi_state = []
result = 0 

for i in range(n):
    app, sign = map(int, sys.stdin.readline().split())
    mi = list(map(int, sys.stdin.readline().split()))
    if app >= sign:
        mi.sort()
        mi_state.append(mi[(app-sign)])
    elif app < sign:
        mi_state.append(1)   # mi_state.append(mi[0]) -> mi_state.append(1)로 수정 후 성공 (수강인원이 신청인원보다 많을 경우는 수업을 다 들을 수 있으므로 마일리지 1점만 소모) 

mi_state.sort()

for i in mi_state:
    if m - i >= 0:
        result += 1
        m -= i
    else:
        break
        
print(result)