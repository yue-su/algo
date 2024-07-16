""" Given the root of a binary tree, return the lowest common ancestor(LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundP = False
        foundQ = False

        def find(root, p, q):
            nonlocal foundP
            nonlocal foundQ

            if not root:
                return None

            left = find(root.left, p, q)
            right = find(root.right, p, q)
            # post-order, visit all the node 
            if root == p or root == q:
                if root == p:
                    foundP = True
                if root == q:
                    foundQ = True
                return root

            if left and right:
                return root

            if not left and not right:
                return None

            return left if left else right

        res = find(root, p, q)
        if foundP and foundQ:
            return res
        else:
            return None
