# 풀이
def solution(nums, target):
    rest = {}
    rest[nums[0]] = 0
    answer = []
    for i in range(1, len(nums)):
        if target-nums[i] in rest:
            answer = [rest[target-nums[i]], i]
            break
        rest[nums[i]] = i

    return answer

nums = [2,7,5,11,14]
nums = [3,2,4]
target = 9
target = 6
print(solution(nums, target))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         rest = defaultdict()
#         rest[nums[0]] = 0
#         answer = []
#         for i in range(1, len(nums)):
#             if target-nums[i] in rest:
#                 answer = [rest[target-nums[i]], i]
#                 break
#             rest[nums[i]] = i

#         return answer