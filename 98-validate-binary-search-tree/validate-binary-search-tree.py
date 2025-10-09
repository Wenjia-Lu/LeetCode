# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        valid = True
        def helper(root):
            if not root:
                return True
            nonlocal prev
            nonlocal valid
            helper(root.left)
            valid = valid and prev < root.val
            prev = root.val
            helper(root.right)
        
        helper(root)
        
        return valid