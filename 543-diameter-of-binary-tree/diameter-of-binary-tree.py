class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def depth(root):
            nonlocal longest
            if root == None:
                return 0
            if root.left == root.right == None:
                return 1
            left = depth(root.left)
            right = depth(root.right)
            longest = max(longest, left + right)
            return max(left, right) + 1
        depth(root)
        return longest
