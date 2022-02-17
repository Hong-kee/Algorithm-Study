# Sol1
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        print(head)
        if head == None or head.next == None:
            return head
        head.next.val, head.val = head.val, head.next.val
        head.next.next = self.swapPairs(head.next.next)
        return head

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     # def get_Next(self, ListNode):
#     #     self.next = ListNode
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
#         head.next.val, head.val = head.val, head.next.val
#         head.next.next = self.swapPairs(head.next.next)
#         return head

# data = [1,2,3,4]
# head = ListNode()
# head.val = data[-1]
# print(head)

# for i in range(len(data)-2, 0, -1):
#     head.next = head
#     head.val = data[i]

# print(head.val, head.next)
# Solution = Solution()
# print(Solution.swapPairs(head))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
