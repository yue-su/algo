class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    # Write your code here.
    def dfs(root, maxVal, minVal):
        if not root:
            return True
        
        if root.value > maxVal or root.value < minVal:
            return False
        
        return dfs(root.left, root.value, minVal) and dfs(root.right, maxVal, root.value)
    
    return dfs(root, float('inf'), float('-inf'))


# Test Cases
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)),
                 TreeNode(10, None, TreeNode(14, TreeNode(13))))
tree4 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(9)),
                 TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(is_valid_bst(None), True)
print(is_valid_bst(tree1), True)
print(is_valid_bst(tree2), False)
print(is_valid_bst(tree3), True)
print(is_valid_bst(tree4), False)
