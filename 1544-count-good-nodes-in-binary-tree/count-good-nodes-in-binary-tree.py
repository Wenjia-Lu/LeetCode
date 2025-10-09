# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = [0]
        def helper(root, large):
            if not root:
                return
            
            large = max(large, root.val)
            if large <= root.val:
                print(root.val, large)
                good[0] += 1
            helper(root.left, large)
            helper(root.right, large)

        helper(root, float('-inf'))
        return good[0]

# large = 3
# good = 1
# root = 3