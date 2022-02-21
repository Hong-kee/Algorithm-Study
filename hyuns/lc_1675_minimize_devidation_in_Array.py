class Solution:
    def minimumDeviation(self, nums: list()) -> int:
        import heapq
        mx_heap = []
        for num in nums:
            if num%2 != 0:
                num *= 2
            
            heapq.heappush(mx_heap, num)
        
        mn, mx = max(mx_heap)[1], min(mx_heap)[1]
        answer = abs(mx-mn)
        
        while mx%2==0:
            hp = heapq.heappop(mx_heap)[1] // 2
            heapq.heappush(mx_heap, (-hp, hp))
            mx = mx_heap[0][1]
            answer = min(answer, abs(mx-mn))
        
        print(answer)
        return answer

# [1,2,3,4]
# [6,5]
# [2,8,6,3]
nums = [5,6]
solution = Solution()
solution.minimumDeviation(nums)