class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, mid, end = 0, len(nums)//2, len(nums)
        while nums[mid] != target:
            if mid == start or mid == end:
                return -1
            if nums[mid] < target:
                start = mid
                mid = (mid + end) // 2
            else:
                end = mid
                mid = (mid + start) // 2
                
        return mid
    
solution = Solution()
nums = [-1,0,3,5,9,12]
target = 2

# nums = [-1,0,3,5,9,12]
# target = 9
print(solution.search(nums, target))