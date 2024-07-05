""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, return the in -order traversal of its nodes' values. You must use iterative approach.

In-order traversal:
1. Traverse the left subtree.
2. Visit the root.
3. Traverse the right subtree.

Example:
• Given a binary tree:
           1
          / \
         2   3
// returns [2, 1, 3]

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ """
from test_case import TreeNode, Test


def inOrderTraversal(root: TreeNode) -> [int]:
    # Write your code here.
    stack = [root]
    res = []

    if not root:
        return res

    while True:
        if not stack:
            return res
        while root.left:
            stack.append(root.left)
            root = root.left
        node = stack.pop()
        res.append(node.value)
        if node.right:
            stack.append(node.right)
            #reset the root to have the left nodes appened in the stack
            root = node.right


test = Test()
# Test Cases
test.startProblem("In-Order Traversal")
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree3 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(
    9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
test.test([], inOrderTraversal(None), 1)
test.test([2, 1, 3], inOrderTraversal(tree1), 2)
test.test([4, 2, 5, 1, 3], inOrderTraversal(tree2), 3)
test.test([8, 4, 9, 2, 5, 1, 6, 3, 7], inOrderTraversal(tree3), 4)
test.endProblem()
# tree1:
#          1
#        /   \
#       2     3
#
# tree2:
#          1
#        /   \
#       2     3
#      / \
#     4   5
#
# tree3:
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
#    / \
#   8   9
