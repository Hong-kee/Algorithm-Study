from itertools import permutations


from itertools import permutations
from collections import Counter
def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    target, window = Counter(s1), Counter()
    start = 0
    
    for idx, s in enumerate(s2):

        window[s] += 1

        if idx >= len(s1):
            window[s2[start]] -= 1
            if window[s2[start]] == 0: del window[s2[start]]
            start += 1

        if window == target:
            return True
    return False

s1 = input()
s2 = input()
print(checkInclusion(s1, s2))