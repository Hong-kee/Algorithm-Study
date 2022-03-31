# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        sort_list = ListNode(0, head)
        pred = sort_list
        
        def dfs(pred, head):
            
            if head  == None:
                return
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                pred.next = head.next
                dfs(pred, head.next)
            else:
                dfs(pred.next, head.next)
        dfs(pred, head)
        
        return sort_list.next

class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        sort_list = ListNode(0, head)
        pred = sort_list
        
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            
            head = head.next           
            
        return sort_list.next

head = [1,2,3,3,4,4,5]
node = ListNode()
node_head = ListNode(0, node)
while head:
    node.val = head[0]
    head = head[1:]
    if head:
        node.next = ListNode()
        node = node.next
print(node_head.next)

solution = Solution1()
solution.deleteDuplicates(node_head.next)
