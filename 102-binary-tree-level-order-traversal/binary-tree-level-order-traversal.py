# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []

        def level(root, h):
            if not root:
                return
            if len(arr) < h:
                arr.append([])
            arr[h - 1].append(root.val)
            level(root.left, h+1)
            level(root.right, h+1)
            
        level(root, 1)
        
        return arr