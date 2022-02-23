class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n != '0': # prevent leading zeros
                st.append(n)
                
        if k: # not fully spent
            st = st[0:k-1]
            
        return ''.join(st) or '0'

num, k = "9", 1
solution = Solution()
print(solution.removeKdigits(num, k))