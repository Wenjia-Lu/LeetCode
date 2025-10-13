# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(root, path, init=None):
            if not root:
                return
            if root.left == root.right == None:
                path = path + f"->{root.val}"
                result.append(path[2:])
                return
            dfs(root.left, path + f"->{root.val}")
            dfs(root.right, path + f"->{root.val}")

        dfs(root, "")
        return result
        