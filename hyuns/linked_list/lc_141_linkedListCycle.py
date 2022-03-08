# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = fast = head
        while fast and fast.next:
            if fast.next == slow or fast.next == slow:
                return True
            fast = fast.next.next
            slow = slow.next
            
        return False


f_head, pos = [3,2,0,-4], 1
pos_head = None
idx = 0

def dfs(f_head, idx):

    head = ListNode(f_head[0])
    if idx == pos:
        global pos_head
        pos_head = head

    if len(f_head) != 1:
        head.next = dfs(f_head[1:], idx+1)
    elif len(f_head) == 1 and pos_head:
        head.next = pos_head
    return head
head = dfs(f_head, idx)

solution = Solution()
print(solution.hasCycle(head))