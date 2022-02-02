
# 다시 풀이 - 코딩테스트 기출
def dfs(ans, numbers, target):
    if len(numbers) == 0:
        if ans == target:
            return 1
        else:
            return 0
    return dfs(ans+numbers[0], numbers[1:], target) + dfs(ans-numbers[0], numbers[1:], target)

def solution(numbers, target):
    return dfs(numbers[0], numbers[1:], target) + dfs(-numbers[0], numbers[1:], target)
print(solution([1,1,1,1,1], 3))


# 예전 풀이
# def dfs(numbers, target, index, res):
#     if index == len(numbers)-1 and target == res:
#         return 1
#     elif index == len(numbers)-1:
#         return 0
#     index += 1
#     return dfs(numbers, target, index, res + numbers[index]) + dfs(numbers, target,  index, res - numbers[index])
# def solution(numbers, target):
#     index, res = 0, 0
#     return dfs(numbers, target, index, res + numbers[index]) + dfs(numbers, target, index, res - numbers[index])