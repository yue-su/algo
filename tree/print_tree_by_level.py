from utils import Test, TreeNode

def printTree(root: TreeNode) -> [[int]]:
    if root is None:
        return root
    
    res = []
    
    queue = [root]
    while len(queue) > 0:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
  
    return res


test = Test("Print Tree by Level")
# Test Cases
test.startProblem("Print Tree by Level")
test.test([[1], [2, 3]], printTree(TreeNode(1, TreeNode(2), TreeNode(3))), 1)
test.test([[2], [29, 4], [26, 2], [9]], printTree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 2)
test.test([[1], [2, 3], [4, 5]], printTree(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))), 3)
test.test([[-3]], printTree(TreeNode(-3)), 4)
test.endProblem()