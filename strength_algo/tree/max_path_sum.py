""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a non-empty binary tree, find the maximum path sum.

Note:
• A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example:
• Given a binary tree:
           1
          / \    
         2   3
        /     
      -1   
// returns 6 (1 + 2 + 3)

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ """
from test_case import Test, TreeNode


def mps(root: TreeNode) -> int:
    # Write your code here.
    max_sum = float("-inf")

    #dfs returns the max path sum extending from the current root
    def dfs(root):
        nonlocal max_sum
        if not root:
            return 0

        left = max(dfs(root.left), 0)
        right = max(dfs(root.right), 0)

        path_sum = root.value + left + right
        max_sum = max(max_sum, path_sum)

        return root.value + max(left, right)

    dfs(root)
    print(max_sum)
    return max_sum


test = Test()
# Test Cases
test.startProblem("Max Path Sum")
test.test(6, mps(TreeNode(1, TreeNode(2, TreeNode(-1)), TreeNode(3))), 1)
test.test(18, mps(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
          TreeNode(3, TreeNode(6), TreeNode(7)))), 2)
test.test(3, mps(TreeNode(1, TreeNode(2), TreeNode(-4))), 3)
test.test(7, mps(TreeNode(1, TreeNode(-5, TreeNode(6)), TreeNode(5))), 4)
test.test(21, mps(TreeNode(1, TreeNode(-10, TreeNode(3, TreeNode(5, TreeNode(13),
          TreeNode(-1)), TreeNode(-1))), TreeNode(-5, TreeNode(-20), TreeNode(-21)))), 5)
test.endProblem()
