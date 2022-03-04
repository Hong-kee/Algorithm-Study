class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # solution 봄
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        dp[0][0] = poured # 모두 부어놓고 나누기
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                temp = (dp[i][j] - 1) / 2.0 # 현재 dp에서 1만큼 부어지고 다음 dp에 반씩 나눠서 옮겨짐
                if temp > 0:    # 현재 dp가 1보다 작을 경우, 다음 dp에 못 넘겨준다.
                    dp[i + 1][j] += temp
                    dp[i + 1][j + 1] += temp
        
        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1 # dp가 1보다 많을 경우, 채워졌으므로 1로 return

solution = Solution()
solution.champagneTower(poured=4,query_row=3,query_glass=1)