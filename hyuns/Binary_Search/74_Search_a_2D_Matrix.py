class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        m, n = len(matrix[0]), len(matrix)
        start, end = 0, m*n-1
        while start <= end:
            if matrix[start//m][start%m] == target or matrix[end//m][end%m] == target:
                return True
            
            mid = (start + end) // 2
            
            if matrix[mid//m][mid%m] == target:
                return True
            elif matrix[mid//m][mid%m] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

#         row = matrix[0]
#         for m in matrix:
#             if m[0] > target:
#                 break
#             else:
#                 row = m
        
#         left, right = 0, len(row)-1
#         while left <= right:
#             if row[left] == target or row[right] == target:
#                 return True
            
#             mid = (left + right) // 2
            
#             if row[mid] == target:
#                 return True
#             elif row[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         return False

matrix, target  = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3

solution = Solution()
print(solution.searchMatrix(matrix, target))