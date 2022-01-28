'''

a의 b제곱 했을 때, 끝에 다섯자리수 출력하자.

a는 10,000,000,000,000 이하의 자연수
b는 10,000,000,000,000 이하의 자연수

'''

data = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]
result = []


def solution(a, b):
    

    # 효율성 실패
    # answer = 1

    # for _ in range(b):
    #     answer *= a
    #     if answer > 99999:
    #         answer %= 100000

    answer = 1

    # 효율성 성공
    while b != 0:
        if b % 2 != 0:
            answer = (answer * a) % 100000
        b //= 2
        a = (a * a) % 100000   

    return answer

print(solution(5, 21))
print(solution(2, 24))
    

