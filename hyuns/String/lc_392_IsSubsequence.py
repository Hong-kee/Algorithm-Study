class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ch = ""
        pos = 0
        if not s:
            return True
        if not t:
            return False
        
        for st in t:
            if s[pos] == st:
                ch += st
                pos += 1

                if ch == s:
                    return True
        
        return False