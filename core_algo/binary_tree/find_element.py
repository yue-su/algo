class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_bfs(root: TreeNode, target: int) -> bool:
    # Write your code here.
    if not root:
        return False
    q = [root]
    while q:
        node = q.pop(0)
        if node.value == target:
            return True
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return False


# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)),
                 TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_bfs(None, 1), False)
print(find_bfs(tree1, 9), True)
print(find_bfs(tree1, 1), False)
print(find_bfs(tree1, 2), True)
print(find_bfs(TreeNode(1), 2), False)


def find_dfs(root: TreeNode, target: int) -> bool:
    # Write your code here.
    if not root:
        return False

    if root.value == target:
        return True

    return find_dfs(root.left, target) or find_dfs(root.right, target)


# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)),
                 TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_dfs(None, 1), False)
print(find_dfs(tree1, 9), True)
print(find_dfs(tree1, 1), False)
print(find_dfs(tree1, 2), True)
print(find_dfs(TreeNode(1), 2), False)
