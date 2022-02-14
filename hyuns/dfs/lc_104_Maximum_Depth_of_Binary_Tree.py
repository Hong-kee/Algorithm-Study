# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#sol 2.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

#sol 1.
def dfs(root, sums):
    
    if root != None:
        return max(dfs(root.left, sums+1), dfs(root.right, sums+1))
    else:
        return sums

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root, 0)