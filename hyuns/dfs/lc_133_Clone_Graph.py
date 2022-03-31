
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        
        new_neighbors = []
        for neighbor in node.neighbors:
            if neighbor.val == 1 or neighbor.val == node.val:
                new_neighbors.append(neighbor)
            else:
                new_neighbors.append(self.cloneGraph(neighbor))

        return Node(node.val, new_neighbors)

node = Node()
solution = Solution()

node.val = 1
node.neighbors = [node.val+1, ]
solution.cloneGraph