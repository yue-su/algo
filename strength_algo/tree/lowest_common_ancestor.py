""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, find the lowest common ancestor of two given nodes in the tree and return its value. A node can be its own ancestor.

Examples:
• Given a binary tree:
                     10
                    /  \
                  5     12
                 / \    /    
                3   6  11
• For node1: 3, node2: 6 // returns 5
• For node1: 11, node2: 6 // returns 10

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ """
from test_case import TreeNode, Test


def find(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None

    if root.val == val:
        return root

    left = find(root.left, val)
    if left:
        return left
    right = find(root.right, val)
    if right:
        return right


def lowestCommonAncestor2(root: TreeNode, node1: TreeNode, node2: TreeNode) -> int:
    # Write your code here.
    def find(root, val):
        if not root:
            return None

        if root.value == val:
            return root

        left = find(root.left, val)
        if left:
            return left
        right = find(root.right, val)
        if right:
            return right

        return None

    if not root:
        return root

    if root == node1 or root == node2:
        return root.value

    if find(root.left, node1.value) and find(root.left, node2.value):
        return lowestCommonAncestor(root.left, node1, node2)

    if find(root.right, node1.value) and find(root.right, node2.value):
        return lowestCommonAncestor(root.right, node1, node2)

    return root.value


def lowestCommonAncestor(root: TreeNode, node1: TreeNode, node2: TreeNode) -> int:
    if not root:
        return root

    if root == node1 or root == node2:
        return root.value

    left = lowestCommonAncestor(root.left, node1, node2)
    right = lowestCommonAncestor(root.right, node1, node2)

    if left and right:
        return root.value

    if left:
        return left
    if right:
        return right


test = Test()

# Test Cases
test.startProblem("Lowest Common Ancestor")
tree1 = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(6)),
                 TreeNode(12, TreeNode(11)))
test.test(5, lowestCommonAncestor(tree1, tree1.left.left, tree1.left.right), 1)
test.test(10, lowestCommonAncestor(
    tree1, tree1.right.left, tree1.left.right), 2)
test.test(10, lowestCommonAncestor(tree1, tree1.left.right, tree1), 3)
test.test(12, lowestCommonAncestor(tree1, tree1.right, tree1.right.left), 4)
test.test(10, lowestCommonAncestor(
    tree1, tree1.left.right, tree1.right.left), 5)
test.endProblem()
