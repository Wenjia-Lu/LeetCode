# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 24 + 7
# 4 -> 2 -> None
# 7 -> None
# dummy ->
# ans^
# c = 11
# d =  11


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        carry = 0
        while l1 or l2 or carry:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            c = a + b + carry
            if c > 9:
                c -= 10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(c)
            dummy = dummy.next
        return ans.next
        

