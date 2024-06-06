class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def count_tree(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = [root]
    res = 0

    while queue:
        node = queue.pop(0)
        res += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return res


# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)