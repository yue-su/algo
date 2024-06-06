'''
❓ PROMPT
Convert a sorted array into a balanced binary search tree. Return the root of the created tree.

Example(s)
Input:  [1, 2, 3, 4, 5] =>

Output:
        3
   2        5
1        4

or
        3
    2       4
1              5

or
    3
1       5
   2  4

or
   3
1     4
   2     5
 

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
function sortedArrayToBST(nums) {
def sortedArrayToBST(nums: list[int]) -> TreeNode:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

from collections import deque

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list[int]) -> TreeNode:
   if not nums:
      return None
   
   def construct(start, end):
      if start > end:
         return None
      mid = start + (end - start) // 2
      root = TreeNode(nums[mid])
      root.left = construct(start, mid-1)
      root.right = construct(mid+1, end)
      return root
   
   return construct(0, len(nums)-1)

def printTree(root: TreeNode):
    if not root:
        print("Tree is empty")
        return

    # Use a queue for level-order traversal
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("null", end=" ")
    print()

# Test cases
nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 2, 3, 4, 5, 6, 7]
nums3 = []
nums4 = [1]

root1 = sortedArrayToBST(nums1)
root2 = sortedArrayToBST(nums2)
root3 = sortedArrayToBST(nums3)
root4 = sortedArrayToBST(nums4)

print("Tree for nums1:")
printTree(root1)
print("Tree for nums2:")
printTree(root2)
print("Tree for nums3:")
printTree(root3)
print("Tree for nums4:")
printTree(root4)


'''''''''''''''''''''''''''''''''''''''
This code is intentionally obfuscated
'''''''''''''''''''''''''''''''''''''''
def isCorrect(r): return b(r) and v(r)
def gH(r): 
  if r == None: return 0
  lH=gH(r.left)
  if lH==-1: return -1
  rH=gH(r.right)
  if rH==-1: return -1
  if abs(lH-rH)>1: return -1
  return max(lH,rH)+1
def b(r):return gH(r)!=-1
import sys
def v(r): return vx(r,~sys.maxsize,sys.maxsize)
def vx(r,m,M):
  if r==None: return True
  if r.val>=M or r.val<=m: return False
  return vx(r.left,m,r.val) and vx(r.right,r.val,M)

tests = [
  [1, 2, 3, 4, 5],
  [-10, -3, 0, 5, 9], 
  [],
  [1],
  [1,2],
  [1,2,3,4,5],
  [1,2,10,20,35,50,420,609],
  [-100,-50,-25,-20,-10,-1,0,1,2,10,20]
]

for params in tests:
    actual = sortedArrayToBST(params)
    if isCorrect(actual) != True:
        print(f"Test failed for {params}. Actual: {actual}")
    else:
        print(f"Works fine for {params}.")