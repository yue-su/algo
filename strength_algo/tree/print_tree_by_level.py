""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, print level order traversal so that nodes of all levels are printed in several lines

Examples:
• Given a binary tree:
                 1
                / \ 
               2   3
// returns [[1], [2, 3]]

• Given a binary tree:
                 1
                / \
               2   3
              / \
             4   5

// returns [[1], [2, 3], [4, 5]]

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ """
from test_case import Test, TreeNode


def printTree(root: TreeNode) -> [[int]]:
    # Write your code here.
    pass


test = Test("")
# Test Cases
test.startProblem("Print Tree by Level")
test.test([[1], [2, 3]], printTree(TreeNode(1, TreeNode(2), TreeNode(3))), 1)
test.test([[2], [29, 4], [26, 2], [9]], printTree(TreeNode(2, TreeNode(
    29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 2)
test.test([[1], [2, 3], [4, 5]], printTree(
    TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))), 3)
test.test([[-3]], printTree(TreeNode(-3)), 4)
test.endProblem()
