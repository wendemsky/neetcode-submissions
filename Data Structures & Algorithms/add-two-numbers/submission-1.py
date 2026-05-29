# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = i = 0
        cur1 = l1
        while cur1:
            num1 += cur1.val * (10 ** i)
            i += 1
            cur1 = cur1.next
        num2 = i = 0
        cur2 = l2
        while cur2:
            num2 += cur2.val * (10 ** i)
            i += 1
            cur2 = cur2.next
        res = num1 + num2
        l3 = ListNode(0)
        cur3 = l3
        if res == 0:
            return l3
        while res:
            num = res % 10
            print("num: ", num)
            dummy = ListNode(num)
            cur3.next = dummy
            res = res // 10
            print("res: ", res)
            cur3 = cur3.next 

        return l3.next
        