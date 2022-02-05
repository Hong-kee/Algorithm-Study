'''
Contiguous Subarray : 연속 부분 행렬
문제는 0와 1의 개수가 같은 Contiguous Subarray를 구하라 함.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        sum = 0
        max_length = 0
        hash_table = {0:-1}
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
                
            if sum in hash_table:
                max_length = max(max_length, i - hash_table[sum])
            else:
                hash_table[sum] = i
                
        return max_length