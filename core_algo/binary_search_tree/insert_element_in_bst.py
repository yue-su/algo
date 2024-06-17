class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayify_tree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array


def insert_bst(root: TreeNode, target: int) -> TreeNode:
    # Write your code here.
    if not root:
        return TreeNode(target)

    if target < root.value:
        root.left = insert_bst(root.left, target)
    else:
        root.right = insert_bst(root.right, target)

    return root


# Test Cases
tree = TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(arrayify_tree(insert_bst(tree, 7)))  # [6, 3, 8, 2, 4, 7]
print(arrayify_tree(insert_bst(tree, 5)))  # [6, 3, 8, 2, 4, 7, 5]
print(arrayify_tree(insert_bst(tree, 1)))  # [6, 3, 8, 2, 4, 7, 1, 5]
print(arrayify_tree(insert_bst(None, 1)))  # [1]

# Given tree:
#              6
#            /   \
#           3     8
#          / \    /
#         2   4  7
#        /     \
#       1       5
