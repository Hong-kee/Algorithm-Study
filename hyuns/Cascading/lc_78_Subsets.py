class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = [[]]
        for num in nums:
            answer += [i + [num] for i in answer]
        return answer

        # answer = []
        # for i in range(len(nums)+1):
        #     for c in combinations(nums, i):
        #         answer.append(list(c))
        # return answer