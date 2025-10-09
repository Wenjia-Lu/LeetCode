# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []

        # time: O(n), traverses each node
        # space: O(n) worst case (a stack for each node)
        def helper(root, h):
            if root:
                if len(view) == h:
                    view.append(root.val)
                else:
                    view[h] = root.val
            else:
                return
            helper(root.left, h+1)
            helper(root.right, h+1)

        helper(root, 0)
        return view

# 1, 2, 5