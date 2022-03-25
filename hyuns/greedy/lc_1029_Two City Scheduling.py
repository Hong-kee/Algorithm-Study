class Solution:
    def twoCitySchedCost(self, costs: list(list())) -> int:
        costs = sorted(costs, key=lambda x: (x[0]-x[1]))
        ans = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]

        return ans
    
solution = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
print(solution.twoCitySchedCost(costs))