# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        r = l = head
        for i in range(k-1):
            r = r.next
        tail = r
        while tail.next:
            tail, l = tail.next, l.next
        
        l.val, r.val = r.val, l.val
        
        return head
# my Solution
#         headList = []
#         def dfs(headList, head):
#             if not head:
#                 return
#             headList.append(head)
#             dfs(headList, head.next)
#         dfs(headList, head)
        
#         headList[k-1], headList[-1-(k-1)] = headList[-1-(k-1)], headList[k-1]
        
#         for i in range(len(headList)):
#             if i == len(headList)-1:
#                 headList[i].next = None
#             else:
#                 headList[i].next = headList[i+1]
#         return headList[0]

head = [1,2,3,4,5]
k = 2
# head = [7,9,6,6,7,8,3,0,9,5]
# k = 5
head = head[::-1]
newhead = ListNode(head[0], None)
idx = 1
while idx != len(head):
    newhead = ListNode(head[idx],newhead)
    idx += 1

solution = Solution()
print(solution.swapNodes(newhead, k))



        