class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def search_bst(root: TreeNode, target: int) -> bool:
    if not root:
        return False

    if root.value == target:
        return True

    if root.value > target:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)


# Test Cases
tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)),
                TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(search_bst(None, 1), False)
print(search_bst(tree, 1), True)
print(search_bst(tree, 14), True)
print(search_bst(tree, 2), False)
print(search_bst(tree, 13), True)

# Given tree:
#                   8
#                 /   \
#                3     10
#               / \      \
#              1   6      14
#                        /
#                      13
