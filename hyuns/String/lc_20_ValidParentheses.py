class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        check = ["[]", "{}", "()"]

        for i in s:
            if stack and (stack[-1] + i) in check:
                stack = stack[:-1]
            else:
                stack.append(i)

        return True if not stack else False

s = "()[]{}"
solution = Solution()
solution.isValid(s)