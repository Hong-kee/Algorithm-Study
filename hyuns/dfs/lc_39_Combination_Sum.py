from torch import combinations

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(sums , index, path):
            if sums > target:
                return
            elif sums == target:
                res.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(sums+candidates[i], i, path+[candidates[i]])

        dfs(0, 0, [])
        return res

candidates = [2,3,5]
target = 8
solution = Solution()
ans = solution.combinationSum(candidates, target)
print(ans)