# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # increment right by n
        while n > 0 and right:
            right = right.next
            n -= 1
        # increment both pointers till right 
        while right:
            left = left.next
            right = right.next
        # delete the left.next node
        left.next = left.next.next

        return dummy.next
