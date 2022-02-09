'''
https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/1756925/Python-Easy-Short-Solution
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums_count = Counter(nums)
        if k == 0:
            for i in set(nums): nums_count[i] -= 1 
        return sum(nums_count[i+k] > 0 for i in set(nums))

# from collections import Counter
# def solution(nums, k):

#     nums_count = Counter(nums)
#     if k == 0:
#         for i in set(nums): nums_count[i] -= 1 
#     return sum(nums_count[i+k] > 0 for i in set(nums))