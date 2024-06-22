
'''
Given a binary search tree where all nodes have integer values, return the floor and ceiling of a target number.

The floor is the largest element that is smaller than or equal to the target, and the ceil is the smallest element that is greater than or equal to the number.
 

EXAMPLE(S)
  3
1   5

tree = TreeNode(3, 
         TreeNode(1),
         TreeNode(5))

target: 4 returns [3, 5]
target: 2 returns [1, 3]
target: 3 returns [3, 3]


target: 9 returns [5, None]
target: 0 returns [None, 1]

                30
        15              45
    10     17       35      55
  4  11  16  19   32  37  50  70
  
target = 36
floor = 35 <= 30
ceil = 37 <= 45  

  
target = 5 => [4, 10]
target = 3 => [None, 4]
target = 36


floor(target, tree)
  if not tree, return None
- if tree.val == target, return target
  if target < tree.val, return node.value
  if target > tree.val, return floor(target, tree.right)

ceil(target, tree)
- 

dfs(tree, floor=None, ceil=None)
  if not tree, return [floor, ceil]
  if target == tree.val, return [tree.val, tree.val]
  if target > tree.val, return dfs(tree.right, tree.val, ceil)
  if target < tree.val, return dfs(tree.left, floor, tree.val)
 

FUNCTION SIGNATURE
function findFloorAndCeil(node, target):
  return [floor(target, tree), ceil(target, tree)]

'''


class TreeNode:
  def __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def findFloorAndCeil_1(node, target):
  """
  """
  def dfs(tree: TreeNode, floor=None, ceil=None):
    if not tree:
      return [floor, ceil]
    if target == tree.value:
      return [tree.value, tree.value]
    if target > tree.value:
     return dfs(tree.right, tree.value, ceil)
    if target < tree.value:
      return dfs(tree.left, floor, tree.value)
  return dfs(node)
#                30
#        15              45
#    10     17       35      55
#  4  11  16  19   32  37  50  70


def findFloorAndCeil(node: TreeNode, target):
  floor = None
  ceil = None
  if not node:
    return [None, None]
  while node:
    if node.value == target:
      return [target, target]
    if node.value > target:
        ceil = node.value
        node = node.left
    elif node.value < target:
        floor = node.value
        node = node.right
  return [floor, ceil]


#                30
#        15              45
#    10     17       35      55
#  4  11  16  19   32  37  50  70

tree = TreeNode(30,
                TreeNode(15,
                         TreeNode(10,
                                  TreeNode(4),
                                  TreeNode(11)),
                         TreeNode(17,
                                  TreeNode(16),
                                  TreeNode(19))),
                TreeNode(45,
                         TreeNode(35,
                                  TreeNode(32),
                                  TreeNode(37)),
                         TreeNode(55,
                                  TreeNode(50),
                                  TreeNode(70))))

print(findFloorAndCeil(tree, 36) == [35, 37])
print(findFloorAndCeil(tree, 1) == [None, 4])
print(findFloorAndCeil(tree, 400) == [70, None])
print(findFloorAndCeil(None, 1) == [None, None])
print(findFloorAndCeil(tree, 17) == [17, 17])