# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def depth(root):
            if root == None:
                return 0
            if root.left == root.right == None:
                return 1
            left = depth(root.left)
            right = depth(root.right)
            if abs(right - left) >= 2 :
                balanced[0] = False
            return max(left, right) + 1
        depth(root)
        return balanced[0]
            
