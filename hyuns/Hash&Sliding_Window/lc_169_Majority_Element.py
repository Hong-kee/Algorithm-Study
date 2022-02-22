from collections import Counter

from pyparsing import nums
class Solution:
    def majorityElement(self, nums: list(int)) -> int:
        #sol1.
        for x in Counter(nums):
            if Counter(nums)[x] > len(nums)//2:
                return x
        
        
        # sol2.
        # return sorted(num)[len(num)/2]

nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))