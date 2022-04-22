class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # if len(s) < k:
        #     return s[::-1]
        # elif k <= len(s) < 2*k:
        #     return s[:k][::-1] + s[k:]
        # else:
        #     answer = ""
        #     for i in range(0, len(s), 2*k):
        #         answer += s[i:i+k][::-1] + s[i+k:i+2*k]
        #     return answer
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)

s = "abcdefg"
k = 2
solution = Solution()
print(solution.reverseStr(s, k))