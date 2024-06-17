class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_max(root: TreeNode):
    # Write your code here.
    if not root:
        return float("-inf")

    left_max = tree_max(root.left)
    right_max = tree_max(root.right)

    return max(root.value, left_max, right_max)


# Test Cases
print(tree_max(None), float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3)  # 3
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
print(tree_max(TreeNode(1)), 1)
