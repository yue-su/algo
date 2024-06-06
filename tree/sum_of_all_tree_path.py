'''
❓ PROMPT
Given a binary tree, return the sum of all root-to-leaf paths.

Example(s)
     1 <--- root
  2      3
4   5  6   7
sumAllTreePaths(root) == 36

Explanation:
* The leftmost path: 1 + 2 + 4 = 7
* The left-middle path: 1 + 2 + 5 = 8
* The right-middle path: 1 + 3 + 6 = 10
* The rightmost path: 1 + 3 + 7 =  11

Aggregating the paths: 7 + 8 + 10 + 11 = 36
 

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
function sumAllTreePaths(root)
def sumAllTreePaths(root: Node) -> int
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumAllTreePaths(root):
    if not root:
        return 0

    total = 0

    def dfs(root, sum):
        nonlocal total

        if not root:
            return

        sum += root.val

        if not root.left and not root.right:
            total += sum
        
        dfs(root.left, sum)
        dfs(root.right, sum)

        sum -= root.val
    
    dfs(root, 0)

    return total





print(sumAllTreePaths(None) == 0)

oneNode = Node(5)
print(sumAllTreePaths(oneNode) == 5)

#        10
#      10
#    10
#  10
onePath = Node(10, Node(10, Node(10, Node(10))))
print(sumAllTreePaths(onePath) == 40)

#       1
#    2      3
#  4   5  6   7
completeTree = Node(1,
  Node(2,
    Node(4),
    Node(5)),
  Node(3,
    Node(6),
    Node(7)))
print(sumAllTreePaths(completeTree) == 36)

#           30
#     20         40
#  10   25     33   60
#   15 23    32       80
partial4levels = Node(30,
  Node(20,
    Node(10,
      None,
      Node(15)),
    Node(25,
      Node(23),
      None)),
  Node(40,
    Node(33,
      Node(32),
      None),
    Node(60,
      None,
      Node(80))))
print(sumAllTreePaths(partial4levels) == 518)

#          30
#     20     40
#  10   25     60
#      23        80
unevenTree = Node(30,
  Node(20,
    Node(10),
    Node(25,
      Node(23))),
  Node(40,
    None,
    Node(60,
      None,
      Node(80))))
print(sumAllTreePaths(unevenTree) == 368)