# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or k == 0 or (not head.next):
            return head

        new_tail = head
        tail = ListNode(0, head)

        length = 0
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k%length
        
        if k == 0:
            return head

        for _ in range(length-k-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
        
        
head = [1,2,3,4,5]
k = 2
node = ListNode()
node_head = ListNode(0, node)
while head:
    node.val = head[0]
    head = head[1:]
    if head:
        node.next = ListNode()
        node = node.next

solution = Solution()

print(solution.rotateRight(node_head.next, k))
