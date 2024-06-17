class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_tree(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return 0

    left = sum_tree(root.left)
    right = sum_tree(root.right)

    return root.value + left + right


# Test Cases
print(sum_tree(None), 0)
print(sum_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
print(sum_tree(TreeNode(1)), 1)
