class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l, r = 0, len(height)-1
        answer = 0
        while l != r:
            if height[l] <= height[r]:
                answer = max(answer, height[l] * (r-l))
                l += 1
            else:
                answer = max(answer, height[r] * (r-l))
                r -= 1
        return answer

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))