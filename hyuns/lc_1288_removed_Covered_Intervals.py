class Solution:
    def removeCoveredIntervals(self, intervals: list(list())) -> int:
        # another solution
        res, longest = len(intervals), 0
        srtd = sorted(intervals, key = lambda i: (i[0], -i[1]))
        
        for start, end in srtd:
            if end <= longest:
                res -= 1
            else:
                longest = end


## my Solution
#         remove = [True] * len(intervals)        

#         index = 0
#         while index != len(intervals):
#             bx, by = intervals[index]
#             for i in range(len(intervals)):
#                 x,y = intervals[i]
#                 if i == index or remove[i] == False:
#                     continue
#                 if bx <= x and y <= by:
#                     remove[i] = False

#             index += 1

#         return sum(remove)
                
        return res

intervals = [[1,4],[1,5],[3,6]]
solution = Solution()
solution.removeCoveredIntervals(intervals)