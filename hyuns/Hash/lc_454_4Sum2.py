
# 풀이 2 - Hash Table
# 최대 복잡도 (N/2)^2 -> N^2 -> 10,000 까지 나옴
from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        answer = 0
        AB = Counter()
        for a in nums1:
            for b in nums2:
                AB[a+b] += 1
    
        for c in nums3:
            for d in nums4:
                answer += AB[-c-d]
        return answer
                

# '''
# 풀이 1 - dfs
# 1 <= n <= 200
# -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
# dfs로 풀면 최대 N^N -> 200^4,즉, 최대 복잡도 16억 XXXXXXX
# '''
# class Solution:
#     def __init__(self):
#         self.answer = 0
       
#     def dfs(self, ans, nums, n):
#         if n == 3:
#             if ans == 0:
#                 self.answer += 1
#             return
#         nums_i = nums[n]
#         for i in range(len(nums_i)):
#             self.dfs(ans+nums_i[i], nums, n+1)

#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         n = len(nums1)
#         nums = [nums2, nums3, nums4]

#         for i in range(n):
#             self.dfs(nums1[i], nums, 0)

#         return self.answer
    
    

