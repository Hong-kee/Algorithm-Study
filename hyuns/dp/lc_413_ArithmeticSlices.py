class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        answer = 0
        dp = [0] * (len(nums))
        for i in range(2, len(nums)):
            if nums[i-1]-nums[i-2] == nums[i]-nums[i-1]:
                dp[i] = dp[i-1] + 1
            
            answer += dp[i]
        
        return answer
#         Sol1
#         answer = 0
#         if len(nums) < 3:
#             return 0
        
#         for i in range(len(nums)-2):
#             length = 1
#             while i+length != len(nums):
#                 if length == 1:
#                     interval = nums[i+length] - nums[i]
#                 else:
#                     if (nums[i+length] - nums[i]) != interval * length:
#                         break
#                     else:
#                         answer += 1
                        
#                 length += 1
        
#         return answer
                
                    