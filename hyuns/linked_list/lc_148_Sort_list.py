# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        hash_table = {}
        
        def dfs(head):
            
            if head.next == None:
                return head
            
            if not head in hash_table:
                if head.val <= head.next.val:
                    hash_table[head] = dfs(head.next)
                else:
                    head.val, head.next.val = head.next.val, head.val
                    hash_table[head] = dfs(head.next)
            
            if head.val > hash_table[head].val:
                hash_table[head].val, head.val = head.val, hash_table[head].val
            
            return head
                
        
        return dfs(head)

if __name__ == "__main__":

    head = [4,2,1,3]
    # head = [-1,5,3,4,0]
    head = head[::-1]
    new_head = ListNode(head[0], None)
    idx = 1
    while idx != len(head):
        new_head = ListNode(head[idx], new_head)
        idx += 1

    print(new_head)

    solution = Solution()
    print(solution.sortList(new_head))





