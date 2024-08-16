'''
Given a binary tree, return the deepest node (furthest away child). 

Follow-up: If the Fellow did it recursively, ask them to do it iteratively or vice versa.
 

EXAMPLE(S)
    a
   / \
  b   c
 /
d

returns d
 

FUNCTION SIGNATURE
function deepestNode(root)
'''

"""
Iterative Pseudo

queue = [root]

while queue:
  node = queue.pop(0)
  if not queue and node has no left or right:
    return node

  if node has left:
    queue.append(node.left)
  if node has right:
    queue.append(node.right)

"""

def deepestNode(root):
  if not root:
    return root

  queue = [root]

  while queue:
    node = queue.pop(0)
    if not queue and not node.left and not node.right:
      return node.value

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)


def deepest(root):

  def helper(root):
    if not root:
      return (None, 0)

    if not root.left and not root.right:
      return (root.value, 1)

    left_val, left_level = helper(root.left)
    right_val, right_level = helper(root.right)

    if left_level > right_level:
      return (left_val, left_level + 1)
    else:
      return (right_val, right_level + 1)

  res, level = helper(root)

  return res


class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

root2 = TreeNode(1,
                 left=TreeNode(2,
                               left=TreeNode(3)))

# Test the deepest function
print(deepest(root))  # Should print 7
print(deepest(root2))  # Should print 3
