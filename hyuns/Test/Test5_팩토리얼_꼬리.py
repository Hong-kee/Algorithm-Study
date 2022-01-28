'''

팩토리얼의 꼬리에 있는 0의 개수를 세는 알고리즘 구현

ex)

n = 5, output : 1
n = 15, output : 3
n = 25, output : 6
n = 125, output : 31


알고리즘 ㄱㄱ

'''

def solution(n):
    answer = 0

    while n >= 5:
        n //= 5
        answer += n
    return answer

print(solution(25))

