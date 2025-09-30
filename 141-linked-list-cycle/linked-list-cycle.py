# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ct = 0
        s = set()
        while head and len(s) == ct:
            s.add(head)
            head = head.next
            ct += 1
        # if head is none:
        #   went thru graph w/o cycle
        # else len wrong and is cycle
        return head != None
