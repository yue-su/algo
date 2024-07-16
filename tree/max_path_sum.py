# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, root) -> int:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        current_sum = root.val + max(left, 0) + max(right, 0)

        self.max_sum = max(self.max_sum, current_sum)

        return max(root.val + max(left, right), 0)
