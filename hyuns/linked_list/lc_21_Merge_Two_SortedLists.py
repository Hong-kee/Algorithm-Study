# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        print(list1.val)
        print(list2)
        return list1

list1 = [1,2,3]
list2 = [2,3,4]

list1 = ListNode(list1)
list2 = ListNode(list2)
Sol = Solution(list1, list2)
print(Sol.mergeTwoLists(list1, list2))
        
