class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_height(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return -1

    left = tree_height(root.left)
    right = tree_height(root.right)

    return 1 + max(left, right)


# Test Cases
print(tree_height(None), -1)  # -1
print(tree_height(TreeNode(1, TreeNode(2), TreeNode(3))), 1)  # 1
print(tree_height(TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3)  # 3
print(tree_height(TreeNode()), 0)  # 0
