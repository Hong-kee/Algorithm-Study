# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        answer = ListNode(0)
        answer_list = answer
        carry = 0
        
        while l1 or l2 or carry:
            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            # carry, ret = divmod(val1+val2 + carry, 10) 
            
            ret = (val1+val2+carry) % 10
            carry = (val1+val2+ carry) // 10
            
            answer_list.next = ListNode(ret)
            answer_list = answer_list.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return answer.next


l1 = [2,4,3]
l2 = [5,6,4]

node1, node2 = ListNode(), ListNode()
node1_head, node2_head = ListNode(0, node1), ListNode(0, node2)
while l1:
    node1.val = l1[0]
    l1 = l1[1:]
    if l1:
        node1.next = ListNode()
        node1 = node1.next
while l2:
    node2.val = l2[0]
    l2 = l2[1:]
    if l2:
        node2.next = ListNode()
        node2 = node2.next

solution = Solution()
solution.addTwoNumbers(node1_head.next, node2_head.next)
