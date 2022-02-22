class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer, n = 0, len(columnTitle)
        for ch in columnTitle:
            answer += (ord(ch) - ord("A") + 1) * (26**(n-1))
            n -= 1
        return answer

columnTitle = "AB"
# answer = 28
# columnTitle is in the range ["A", "FXSHRXW"]
solution = Solution()
print(solution.titleToNumber(columnTitle))