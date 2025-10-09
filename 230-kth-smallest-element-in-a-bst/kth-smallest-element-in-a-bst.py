# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0
        i = 0
        def helper(root):
            nonlocal kth
            nonlocal i
            if not root:
                return
            helper(root.left)
            i += 1
            if i == k:
                kth = root.val
                return
            helper(root.right)
        
        helper(root)
        return kth

        