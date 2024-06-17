from typing import List


class Test:
    def __init__(self, test_name=""):
        self.total_count = 0
        self.problem_count = 0
        self.total_score = 0
        self.problem_score = 0
        self.current_problem = ""
        self.failed_problems = []
        print(f"Beginning Test: {test_name}")

    # Test Helpers
    def test(self, expected_outcome, outcome, case_num=0):
        if expected_outcome == outcome:
            return self.passed(case_num)
        return self.failed(case_num)

    def testMultipleCases(self, possible_outcomes, outcome, case_num=0):
        for possible_outcome in possible_outcomes:
            if possible_outcome == outcome:
                return self.passed(case_num)
        return self.failed(case_num)

    def testMatchAny(self, expected_outcome, outcome, case_num=0):
        if self.isEqual(expected_outcome, outcome):
            return self.passed(case_num)
        return self.failed(case_num)

    def isEqual(self, array1, array2) -> bool:
        for a1 in array1:
            a1.sort()
        sortedArray1 = sorted(array1)
        for a2 in array2:
            a2.sort()
        sortedArray2 = sorted(array2)
        return sortedArray1 == sortedArray2

    # Test Logistics
    def startProblem(self, problemName):
        self.current_problem = problemName
        self.problem_score = 0
        self.problem_count = 0
        self.failed_problems = []

    def passed(self, case_num):
        self.total_score += 1
        self.problem_score += 1
        self.problem_count += 1
        self.total_count += 1

    def failed(self, case_num):
        self.problem_count += 1
        self.total_count += 1
        self.failed_problems.append(case_num)

    def endProblem(self):
        print(
            f"\n   {self.current_problem} Score: {self.problem_score} / {self.problem_count}")
        if len(self.failed_problems) > 0:
            print(f"   ** Failed Test Cases: {self.failed_problems}")

    def printFinal(self):
        print(f"\nTotal Score: {self.total_score} / {self.total_count}")


test = Test("Core Algos — Variation Set #4")


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array


################################################################################
# 1. Return the kth from the end of a linked list (count from kth to the end)
#
# Q. Given a linked list and kth position, return the number of nodes
#    between the kth and the end of the list.
#    Note: - You may assume all elements have positive integer value.
#          - If K exceeds the length of the list, return -1 instead
#
################################################################################


def countKthToLast(head: ListNode, k: int) -> int:
    # Write your code here.
    for _ in range(k):
        if head:
            head = head.next
        else:
            return -1

    return k


# Test Cases
test.startProblem("1. Count Kth")
LL1 = ListNode(13, ListNode(1, ListNode(
    5, ListNode(3, ListNode(7, ListNode(10))))))
test.test(1, countKthToLast(LL1, 1), 1)
test.test(3, countKthToLast(LL1, 3), 2)
test.test(6, countKthToLast(LL1, 6), 3)
test.test(-1, countKthToLast(LL1, 7), 4)
test.endProblem()

################################################################################
# 2. Insert an element into an unsorted linked list (before the target value)
#
# Q. Given an unsorted linked list, insert an element before the target element
#    Note: - You may assume there are no duplicates.
#          - You must return the head of the updated linked list.
#
# Example:
#    Given: Linked List: [3, -1, 2, 5], element(to be inserted): 0, target: 2
#    Updated Linked List: [3, -1, 0, 2, 5]
#
################################################################################


def insert2(head: ListNode, element: int, target: int) -> ListNode:
    if not head:
        return None

    if head.value == target:
        new_head = ListNode(element)
        new_head.next = head
        return new_head

    head.next = insert2(head.next, element, target)

    return head


# Test Cases
test.startProblem("2. Insertion Before the Target")
LL3 = ListNode(3, ListNode(-1, ListNode(2, ListNode(5))))
test.test([3, -1, 0, 2, 5], arrayify(insert2(LL3, 0, 2)), 1)
test.test([-4, 3, -1, 0, 2, 5], arrayify(insert2(LL3, -4, 3)), 2)
test.test([3, -1, 0, 2, 1, 5], arrayify(insert2(LL3, 1, 5)), 3)
test.endProblem()

################################################################################
# 3. Count leaf nodes in a binary tree (iterative and recursive)
#
# Q. Given a binary tree, count the number of leaf nodes (elements).
#    Note: Leaf node is a node that does not have any child nodes.
#
################################################################################


def countLeafNodesIterative(root: TreeNode) -> int:
    # Write your code here.
    q = [root]
    counter = 0
    if not root:
        return 0

    while q:
        node = q.pop()
        if not node.left and not node.right:
            counter += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return counter


def countLeafNodesRecursive(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return countLeafNodesRecursive(root.left) + countLeafNodesRecursive(root.right)


# Test Cases
test.startProblem("3. Count Leaf Nodes")
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(
    9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
test.test(0, countLeafNodesIterative(None), 1)
test.test(1, countLeafNodesIterative(TreeNode(1)), 2)
test.test(2, countLeafNodesIterative(tree1), 3)
test.test(5, countLeafNodesIterative(tree2), 4)
test.test(0, countLeafNodesRecursive(None), 5)
test.test(1, countLeafNodesRecursive(TreeNode(1)), 6)
test.test(2, countLeafNodesRecursive(tree1), 7)
test.test(5, countLeafNodesRecursive(tree2), 8)
test.endProblem()

# tree1:
#          1
#        /   \
#       2     3
#

# tree2:
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
#    / \
#   8   9

################################################################################
# 4. Validate a leaf node in a binary search tree
#
# Q. Given a binary search tree and a target integer,
#    check if it is a leaf node.
#
################################################################################


def searchBST(root: TreeNode, target: int) -> bool:
    # Write your code here.
    if not root:
        return False
    
    if root.value == target:
        if not root.left and not root.right:
            return True
        else:
            return False
    
    if root.value > target:
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target)


# Test Cases
test.startProblem("4. Validate Leaf Node")
tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(
    4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
test.test(False, searchBST(None, 1), 1)
test.test(True, searchBST(tree, 1), 2)
test.test(False, searchBST(tree, 3), 3)
test.test(True, searchBST(tree, 4), 4)
test.test(True, searchBST(tree, 7), 5)
test.test(False, searchBST(tree, 8), 6)
test.test(True, searchBST(tree, 13), 7)
test.test(False, searchBST(tree, 14), 8)
test.test(False, searchBST(tree, 6), 9)
test.test(True, searchBST(TreeNode(), 0), 10)
test.endProblem()

# tree:
#           8
#         /   \
#        /     \
#       3      10
#      / \       \
#     1   6      14
#        / \     /
#       4   7   13

################################################################################

test.printFinal()
