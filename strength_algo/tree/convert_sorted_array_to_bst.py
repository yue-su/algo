""" 
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of integers sorted in ascending order, convert it to a height balanced BST.

Note:
• A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
• You must pick the smaller number when picking the "middle." In other words, when there are two numbers to choose from to pick the next child node, choose the smaller value(see example below).

Example:
• Given an array: [-10, -3, 0, 5, 9]
// returns:
                0
               / \    
             -10   5 
               \    \
               -3    9

1. Choose 0 as a root node.
2. For left child node of 0, you have -10 and -3. According to the rule, you choose the smaller value -10.
3. Similar for choosing the right child node of 0, you are left with 5 and 9. Since 5 is smaller than 9, 5 becomes the right child node.

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
from test_case import Test, TreeNode, arrayifyTree


def sortedArrayToBST(nums: list[int]) -> TreeNode:
    # Write your code here.
    left = 0
    right = len(nums) - 1

    def build(left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])

        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)

        return node

    return build(left, right)


test = Test("")
# Test Cases
test.startProblem("Convert Sorted Array to BST")
test.test([2, 1, 3], arrayifyTree(sortedArrayToBST([1, 2, 3])), 1)
test.testMultipleCases([[0, -3, 9, -10, 5], [0, -10, 9, -3, 5], [0, -10, 5, -3, 9],
                       [0, -3, 5, -10, 9]], arrayifyTree(sortedArrayToBST([-10, -3, 0, 5, 9])), 2)
test.test([], arrayifyTree(sortedArrayToBST([])), 3)
test.endProblem()
