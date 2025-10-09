# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = [0, 0] # [kth number, current index]
        def helper(root):
            if not root:
                return
            helper(root.left)
            arr[1] += 1
            if arr[1] == k:
                arr[0] = root.val
                return
            helper(root.right)
        
        helper(root)
        return arr[0]

        