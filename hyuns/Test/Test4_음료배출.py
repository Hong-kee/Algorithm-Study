'''

최대 N개까지 동시에 음료수를 생산하는 공장이 있음.
이 공장에서 음료수를 만들 때, 음료수가 만들어지는 순서를 구하려 함.

M개의 음료수를 만들어야할 때, 각각 번호가 붙어음. 번호 별로 만드는 시간이 다를 수 있음
번호 순서대로 음료수 만들어지는 시간 (drink_times)이 주어어질 때, 완성되는 순서대로 번호별로 배열에 담는다.

단, 동시에 만들어졌을 경우, 작은 번호가 앞에 오도록 함.

ex) N = 3, drink_times = [3, 1, 1, 4, 2]
output : [2, 3, 1, 5, 4]

시간(초)     음료 제작중 (번호)      완료 순서
0	        [1번, 2번, 3번]	        []
1	        [1번, 2번, 3번]	        []
2	        [1번, 4번, 5번]	        [2번, 3번]
3	        [1번, 4번, 5번]	        [2번, 3번]
4	        [4번, 5번]	            [2번, 3번, 1번]
5	        [4번]	                [2번, 3번, 1번, 5번]
6	        [4번]	                [2번, 3번, 1번, 5번]
7	        []	                    [2번, 3번, 1번, 5번, 4번]


알고리즘 ㄱㄱ

'''

def solution(N, drink_times):
    
    answer = []
    machine = []
    drink = [False for _ in range(len(drink_times))]

    while len(answer) != len(drink_times):
        
        num = 0
        rest_in_machine = N - len(machine)

        data = []
        # machine에 자리가 있고, 안가져온 drink가 있다면,
        if rest_in_machine > 0 and False in drink:
            for idx, dr in enumerate(drink_times):
                if num == rest_in_machine:
                    break
                if drink[idx] == False:
                    drink[idx] = True
                    machine.append([idx, dr])
                    num += 1
        
        # time - 1 machine update -> 다시
        data = []
        machine = sorted(machine, key=lambda x: x[1])
        
        for idx, time in machine:
            if time - machine[0][1] != 0:
                data.append([idx, time - machine[0][1]])
            else:
                answer.append(idx+1)
        machine = data

    return answer

print(solution(3, [3,1,1,4,2]))
    

