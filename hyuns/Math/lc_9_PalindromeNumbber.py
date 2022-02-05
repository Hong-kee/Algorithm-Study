class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
        
#         st_x = str(x)
#         answer = True
        
#         for i in range(len(st_x)//2):
#             if st_x[i] != st_x[len(st_x) - i - 1]:
#                 answer = not answer
#                 break
#         return answer