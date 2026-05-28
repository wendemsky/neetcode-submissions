# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashset
        seen = set()
        c = head
        while c:
            if c in seen:
                return True 
            seen.add(c)
            c = c.next
        return False