class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # #1 Two pointer
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

        # #2 cheating
        # s.reverse()

        # #3 change real memory
        # s[:] = s[::-1]
        
# in-place change