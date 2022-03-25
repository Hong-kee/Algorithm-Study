import sys
from collections import deque

def change_state(time_way, time, answer):
    # A방향, C방향 확인
    if (time_way[0] and not time_way[3]) or (time_way[2] and not time_way[1]):
        # A 방향의 오른쪽 확인 후, 없으면 차량 통과
        if (time_way[0] and not time_way[3]):
            answer[time_way[0].popleft()] = time # 해당 차량 번호에 시간 입력
        # C 방향의 오른쪽 확인 후, 없으면 차량 통과
        if (time_way[2] and not time_way[1]):
            answer[time_way[2].popleft()] = time
            
    # B방향, D방향 확인
    elif (time_way[3] and not time_way[2]) or (time_way[1] and not time_way[0]):
        # B 방향의 오른쪽 확인 후, 없으면 차량 통과
        if (time_way[3] and not time_way[2]):
            answer[time_way[3].popleft()] = time
        # D 방향의 오른쪽 확인 후, 없으면 차량 통과
        if (time_way[1] and not time_way[0]):
            answer[time_way[1].popleft()] = time
            
def time_state(time, way, time_way):
    for idx, (key, value) in enumerate(way.items()):
        if value and value[0][1] <= time: # 현재 시간에 대기 중인 차량 가져오기
            time_way[idx].append(way[key].popleft()[0])
            
    return time_way, way, time

def end_condition(time_way, way):
    # Deadlock 일 경우
    if time_way[0] and time_way[1] and time_way[2] and time_way[3]:
        return False
    
    # 남은 차량 리스트, 현재 시간의 도로 리스트 가 모두 없을 경우
    if (not way["A"] and not way["B"] and not way["C"] and not way["D"]):
        if (not time_way[0] and not time_way[1] and not time_way[2] and not time_way[3]):
            return False
    
    return True

if __name__ == "__main__":
    # N = int(input())
    N = 200000
    input_ary = [(i, "A") for i in range(200000)]
    answer = [-1] * (N+1)
    way = {"A":deque(), "B":deque(), "C":deque(), "D":deque()}
    time = 0
    for i in range(N):
        
        # ti, wi = sys.stdin.readline().split()
        ti, wi = input_ary[i]
        way[wi].append([i+1, int(ti)])
        if i == 0:
            time = int(ti)
    
    # 현재 시간에 도로 위 차량 상태 리스트
    time_way = [deque() for _ in range(4)]
    
    while True:
        # End condition Check
        if not end_condition(time_way, way):
            break
        else:
            # 현재 도로위 차량 리스트 체크
            time_way, way, time = time_state(time, way, time_way)
            # Change
            change_state(time_way, time, answer)
        time += 1
    
    for i in answer[1:]:
        print(i)