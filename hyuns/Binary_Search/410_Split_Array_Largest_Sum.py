# 다시! 이해 제대로 못함.
class Solution:

    def splitArray(self, nums: [int], m: int) -> int:

        def canPartition(largestSum):

            groups = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largestSum:
                    groups += 1
                    curSum = num
            return groups <= m

        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canPartition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

nums, m= [1,2,3,4,5], 2
solution = Solution()
print(solution.splitArray(nums, m))