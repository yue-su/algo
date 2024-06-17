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


test = Test("Core Algos — Variation Set #1")


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
# 1. Monotonically Increasing Linked List
#
# Q. Given a linked list, determine if it is monotonically increasing (iterative)
#    Note: Monotonically increasing means always increasing or remaining constant
#
# Examples:
#     Given a linked list: 1 -> 1 -> 2 -> 5    // returns True
#     Given a linked list: -1 -> -5 -> 3 -> -100    // returns False
#
################################################################################


def isIncreasing(head: ListNode) -> bool:
    # Write your code here.
    while head.next:
        if not head.value <= head.next.value:
            return False
        head = head.next
    return True


# Test Cases
test.startProblem("1. Determine Increasing")
LL2 = ListNode(1, ListNode(1))
LL3 = ListNode(1, ListNode(1, ListNode(2, ListNode(5))))
LL4 = ListNode(-1, ListNode(-5, ListNode(-3, ListNode(-100))))
test.test(True, isIncreasing(LL2), 1)
test.test(True, isIncreasing(LL3), 2)
test.test(False, isIncreasing(LL4), 3)
test.endProblem()

################################################################################
# 2. Sum two linked lists of different length
#
# Q. Given two linkd lists of possibly different length, sum elements' value
#    at the same position.
#    Note: - You must return the head of the sum of the lists.
#
# Examples:
#   Input:  LL1: 1->2->5, LL2: 3->4
#   Output: 4->6->5
#
################################################################################


def sumLinkedLists(head1: ListNode, head2: ListNode) -> ListNode:
    # Write your code here.
    if not head1 and not head2:
        return None
    if not head1:
        return head2
    if not head2:
        return head1

    new_head = ListNode(head1.value + head2.value)
    new_head.next = sumLinkedLists(head1.next, head2.next)
    return new_head


# Test Cases
test.startProblem("2. Sum Two Linked Lists")
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(-1, ListNode(3, ListNode(-10)))
LL3 = ListNode(3, ListNode(5))
test.test([0, 6, -5], arrayify(sumLinkedLists(LL1, LL2)), 1)
test.test([4, 8, 5], arrayify(sumLinkedLists(LL1, LL3)), 2)
test.test([0], arrayify(sumLinkedLists(ListNode(0), ListNode(0))), 3)
test.endProblem()

################################################################################
# 3. Bubble Sort (Sort negatives)
# Q. Given an array of intgers, move all negative numbers to the left
#    in the order they appear.
#
# Example:
#     [2, -1, 3, -4, 5] -> [-1, -4, 2, 3, 5]
#
################################################################################


def bubbleSortNegatives(array: [int]) -> [int]:
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < 0:
                continue
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# Test Cases
test.startProblem("3. Bubble Sort: Negatives")
test.test([-1, -4, 2, 3, 5], bubbleSortNegatives([2, -1, 3, -4, 5]), 1)
test.test([-10, -13, 1, 3, 5, 8, 9, 32],
          bubbleSortNegatives([-10, 1, 3, 8, -13, 32, 9, 5]), 2)
test.endProblem()

################################################################################
# 4. Count odd elements in a binary tree (iterative and recursive)
#
# Q. Given a binary tree, count the number of elements with odd values
#    in the tree.
#
################################################################################


def countTreeNodesIterative(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return 0
    q = [root]
    res = 0
    while q:
        node = q.pop()
        if node.value % 2 != 0:
            res += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


def countTreeNodesRecursive(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return 0

    if root.value % 2 == 0:
        return countTreeNodesIterative(root.left) + countTreeNodesIterative(root.right)
    else:
        return countTreeNodesIterative(root.left) + countTreeNodesIterative(root.right) + 1


# Test Cases
test.startProblem("4. Count Odd Tree Nodes")
test.test(0, countTreeNodesIterative(None), 1)
test.test(2, countTreeNodesIterative(TreeNode(1, TreeNode(2), TreeNode(3))), 2)
test.test(2, countTreeNodesIterative(TreeNode(2, TreeNode(
    29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3)
test.test(0, countTreeNodesIterative(TreeNode()), 4)
test.test(0, countTreeNodesRecursive(None), 5)
test.test(2, countTreeNodesRecursive(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
test.test(2, countTreeNodesRecursive(TreeNode(2, TreeNode(
    29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 7)
test.test(0, countTreeNodesRecursive(TreeNode()), 8)
test.endProblem()

################################################################################

test.printFinal()
