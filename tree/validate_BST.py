
'''
❓ PROMPT
Determine if a binary tree is a valid binary search tree.

A binary search tree is a binary tree where for each node, all values in the left subtree are smaller than the current node, and all values in the right subtree are greater than the current node.

Example(s)
     10 <--- root
  5      15
3  7   12  17
isValidBST(root) == True

     30 <--- root
 18      50
3  7   33  77
isValidBST(root) == False
Explanation: 7 is smaller than 18, even though it's the right child.

     30 <--- root
 18      50
3  40   33  77
isValidBST(root) == False
Explanation: 40 is larger than 30, even though it's in the left subtree.

  3 <--- root
1   5
isValidBST(root) == True

    3 <--- root
 1     5
   4
isValidBST(root) == False
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function isValidBST(root) {
def isValidBST(root: Node) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Node) -> bool:
    def isValid(root, minVal, maxVal):
      if not root:
        return True

      if root.val < minVal or root.val > maxVal:
         return False

      return isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal)
    
    isValid(root, float("-inf"), float("inf"))




print(isValidBST(None))
print(isValidBST(Node(5)))

#   5
# 1
print(isValidBST(Node(5, Node(1))))

#   5
# 10
print(isValidBST(Node(5, Node(10))) == False)

#  5
#   10
print(isValidBST(Node(5, right=Node(10))))

#  5
#   1
print(isValidBST(Node(5, right=Node(1))) == False)

#   5
# 1  10
print(isValidBST(Node(5, Node(1), Node(10))))

#   5
# 10  1
print(isValidBST(Node(5, Node(10), Node(1))) == False)

#     10
#   5     15
# 3   7 12   17
root = Node(
  10,
  Node(5,
    Node(3), Node(7)),
  Node(15,
    Node(12), Node(17)))
print(isValidBST(root))

#      10
#   5     15
# 2   16 3   20
root = Node(
  10,
  Node(5,
    Node(2), Node(16)),
  Node(10,
    Node(3), Node(20)))
print(isValidBST(root) == False)

#      10
#   15     20
# 30  40  1  12
root = Node(
  10,
  Node(15,
    Node(30), Node(40)),
  Node(20,
    Node(1), Node(12)))
print(isValidBST(root) == False)

#   10
# 1    20
#  4 15
root = Node(
  10,
  Node(1,
    right=Node(4)),
  Node(20,
    Node(15)))
print(isValidBST(root))

#   10
# 1    20
#  99 99
root = Node(
  10,
  Node(1,
    right=Node(99)),
  Node(20,
    Node(99)))
print(isValidBST(root) == False)