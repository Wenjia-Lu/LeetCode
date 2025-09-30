# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        while head != None:
            # prev exists
            n = ListNode(head.val)
            if prev == None:
                prev = ListNode()
                prev.next = n
            else:
                n.next = prev.next
                prev.next = n
            head = head.next
        return prev.next
# 3 -> 2 -> 1
# head = 3: n = [3], prev.next =  [3]
# haed = 2: n = [2], n.next = prev.next, prev.next = n
# head = 1: n = [1], n.next = prev.next