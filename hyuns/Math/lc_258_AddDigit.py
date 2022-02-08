class Solution:
    def addDigits(self, num: int) -> int:

        # by Math O(1)
        return (num-1) % 9 + 1
            
        # by loop
        # while True:
        #     num = sum([int(i) for i in str(num)])
        #     if num // 10 == 0: return num

'''

num % 9 = sum(num) % 9

Proof

먼저, num-sum(num)을 했을 때, 9로 나누어 떨어진다면, 각 수의 나머지는 같아진다.

num - sum(num)
= 10000 * 1 + 1000 * 8 + 100 * 5 + 10 * 9 + 2 - (1+8+5+9+2)
= 9999 * 1 + 999 * 8 + 99 * 5 + 9 * 9 + 0

어떤 수라도 num-sum(num)을 9로 나누어 떨어진다.  
따라서, 각 수의 9의 나머지는 같다.

여기서 생각해할 조건은, 0과 9일 때이다.

if num == 0, 0
else 1 + (num - 1) % 9

'''