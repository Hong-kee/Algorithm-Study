# Sol - sorting
# Runtime ; 5747ms, Memory 14M

def checkInclusion(self, s1: str, s2: str) -> bool:
    s1 = sorted(s1)
    for i in range(len(s2)-len(s1)+1):
        if sorted(s2[i:i+len(s1)]) == s1:
            return True      
    return False       


# Sol - by ASCII of char, Rolling hash
# Runtime ; 227ms Memory 14.2M

def checkInclusion(s1, s2):

    A = [ord(x) - ord("a") for x in s1]
    B = [ord(x) - ord("a") for x in s2]

    target = [0] * 26
    for i in s1:
        target[i] += 1
    
    window = [0] * 26
    
    for i, s in enumerate(B):

        # Sliding Window

        # add
        window[s] += 1

        # remove
        if i >= len(A):
            target[B[i-len(A)]] -= 1

        # check sliding
        if target == window:
            return True

    return False

s1, s2 = input(), input()
print(checkInclusion(s1, s2))




# Sol - Counter
from collections import Counter
def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    target, window = Counter(s1), Counter()
    
    for idx, s in enumerate(s2):

        # Sliding Window

        # add
        window[s] += 1

        # remove
        if idx >= len(s1):
            window[s1[idx-len(s1)]] -= 1
            if not window[s1[idx-len(s1)]]:
                del window[s1[idx-len(s1)]]

        # check after sliding
        if window == target:
            return True

    return False

s1 = input()
s2 = input()
print(checkInclusion(s1, s2))