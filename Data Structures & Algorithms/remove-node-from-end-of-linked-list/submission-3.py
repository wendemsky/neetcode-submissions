# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head 
        while curr:
            length += 1
            curr = curr.next
        if length < 2:
            return None
        
        curr = head
        prev = None
        for i in range(length - n):
            prev = curr
            curr = curr.next
        
        if prev and prev.next:
            temp = prev.next.next
            prev.next.next = None
            prev.next = temp
        else:
            head = head.next

        return head