from collections import Counter
class Solution:
    def subarraySum(self, nums, k):
        '''
        nums : List[int]
        k : int
        return : int
        '''
        
        count = Counter([0])
        sums, answer = 0, 0

        # sol1
        for i in nums:
            sums += i
            # sums-k means prefix without subarray whose sum equals to k
            # so, if there is prefix in count, there is subarray of k-sum in nums
            answer += count[sums-k]
            count[sums] += 1

        return answer