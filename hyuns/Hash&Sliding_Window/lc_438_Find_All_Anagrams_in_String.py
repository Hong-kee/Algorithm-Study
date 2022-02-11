# Hash & Sliding Window

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []

        if len(s) < len(p):
            return answer

        # p Count, s Count less than p
        p_Counter = Counter(p)
        s_Counter = Counter(s[:len(p)-1])

        # get last s[len(p)], del first s[len(p)]
        for i in range(len(p)-1, len(s)):
            s_Counter[s[i]] += 1
            if s_Counter == p_Counter:
                answer.append(i-len(p)+1)

            s_Counter[s[i-len(p)+1]] -= 1
            if s_Counter[s[i-len(p)+1]] == 0:
                del s_Counter[s[i-len(p)+1]]

        return answer