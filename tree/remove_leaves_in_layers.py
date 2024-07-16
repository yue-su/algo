
'''
Given the root of a binary tree, collect a tree's nodes by level from the leaves up. Return an array of arrays representing the values of the leaves at each iteration.

The result will have the leaves of the tree (no matter the depth from the root) in the first array (index zero), and then the root will be in the last by itself. See the examples below.

The complexity analysis of this one is interesting and might be worth discussing if there is time. What is the best case complexity? Worst case?

Thoroughly understand the problem
Identify possible solution(s)
Choose a solution
Build it
Test it

EXAMPLE(S)
Input:
    1
   / \
  2   3
 / \
4   5

Output:
[[4, 5, 3], [2], [1]]

HLA 1:
Traverse the tree until the tree is empty. If we find a node that has no children( a leaf node), we remove it from the tree and add it to our array of leaves for that level. after each iteration, add the array of leaves to the output.

DFT to find leaf nodes
outer loop:
dft while root

DFT:
return null if leaf
dft calls to explore left and right subtrees
return node if not leaf


HLA 2:
FUNCTION SIGNATURE
def findLeaves(root: TreeNode) -> List[List[int]]:

'''
""" 
    class TreeNode {
constructor(val, left=null, right=null) {
    this.val = val;
    this.left = left;
    this.right = right;
}
}

    const root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.left.left = new TreeNode(4);
    root.left.right = new TreeNode(5);
    // 1-2-3-4-5
    // Run time is On ^ 2
    // Space On
    console.log(findLeaves(root)); // Output: [[4, 5, 3], [2], [1]]
 """




from utils import TreeNode

def findLeaves(root: TreeNode) -> list[list[int]]:
    level_map = {}

    def dfs(root):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        curr_level = 1 + max(left, right)

        if curr_level in level_map:
            level_map[curr_level].append(root.value)
        else:
            level_map[curr_level] = [root.value]

        return curr_level

    dfs(root)

    print(level_map)

    return [item for item in level_map.values()]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(findLeaves(root))
