# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hash(self, root, s):
        if root == None:
            s.append("# ")
            return
        s.append(f"L{root.val}R ")
        self.hash(root.left, s)
        self.hash(root.right, s)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s = []
        t = []
        self.hash(root, s)
        self.hash(subRoot, t)
        s = "".join(s)
        t = "".join(t)
        return t in s