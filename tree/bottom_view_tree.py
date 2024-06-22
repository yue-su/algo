
'''
Given a binary tree where each node holds an integer, write a function that returns an array of integers representing the bottom view of the tree.

To calculate the bottom view of a tree, consider the horizontal distance of each node. The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.  
The horizontal distance of a left child is hd(parent) - 1.  
The horizontal distance of a right child is hd(parent) + 1.
 

EXAMPLE(S)
For this tree, hd(1) = -2, and hd(6) = 0.

           5(0)
        /     \
      3(-1)     7(1)
    /  \      /   \
  1(-2) 4(0) 6(0)  9(2)
 /                /
0(-3)            8(1)

h(0) = -3 h(1) = -2 h(3) = -1 h(4) = 0 h(6) = 0 h(8) = 1 h(9) = 2

The bottom view is either [0, 1, 3, 4, 8, 9] or [0, 1, 3, 4, 6, 8, 9]
 

FUNCTION SIGNATURE
func bottomView(root: Node) -> [Int]

approach:

1. do a dfs and calculate the distance of each node, and save them to a map
    map = [distance, node.val]
    at the each node, we check if the distance is already in the map
    if the distance is already in the map, we update the value to the current node value

2. for the map we print from the least value to the largest. 


'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bottomView(root):

    distances = {}

    def dfs(root, distance, level):

        if not root:
            return

        if distance not in distances or level > distances[distance][1]:
            distances[distance] = (root.val, level)

        dfs(root.left, distance - 1, level + 1)
        dfs(root.right, distance + 1, level + 1)

    dfs(root, 0, 0)

    res = []

    for key in sorted(distances.keys()):
        res.append(distances[key][0])

    return res


tree = TreeNode(0,
                left=TreeNode(3, left=TreeNode(1, left=TreeNode(0)), right=TreeNode(4)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9, left=TreeNode(8))))


print(bottomView(tree))


def tree_bottom_view(root):
    lowest_node_for_distance = {}

    def helper(root, distance, level):
        if not root:
            return
        if distance not in lowest_node_for_distance or level > lowest_node_for_distance[distance][1]:
            lowest_node_for_distance[distance] = (root.val, level)

        helper(root.left, distance - 1, level + 1)
        helper(root.right, distance + 1, level + 1)

    helper(root, 0, 0)

    for key in sorted(lowest_node_for_distance.keys()):
        print(lowest_node_for_distance.get(key)[0], end=' ')
