""" Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. 
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
 """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0
        self.dfs(root, 1001)
        return self.max_path

    def dfs(self, root, prev):
        if not root:
            return 0

        left = self.dfs(root.left, root.val)
        right = self.dfs(root.right, root.val)

        self.max_path = max(self.max_path, left + right)

        if root.val != prev:
            return 0

        return 1 + max(left, right)
