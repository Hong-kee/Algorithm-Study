class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sol2
        # arr = Counter(nums)
        # for i in list(set(nums)):
        #     if arr[i] == 1: return i
        
        # sol1
        res = 0
        for i in nums:
            res^=i # xor
        return res