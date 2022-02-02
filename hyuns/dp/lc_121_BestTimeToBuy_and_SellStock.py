class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, low = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                answer = max(answer, prices[i] - low)
        return answer