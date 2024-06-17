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


test = Test("Core Algos — Variation Set #3")


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
# 1. Return the kth from the end of a linked list (copy kth to the end)
#
# Q. Given a linked list, make a copy of the list from the kth position
#    to the end.
#    Note: - You must return the head of the copied linked list.
#          - You may assume all elements have positive integer value.
#          - If K exceeds the length of the list, return noneType
#            (e.g. None, null, or nil) instead.
#
################################################################################


def copyKthToLast(head: ListNode, k: int) -> ListNode:
    # Write your code here.
    def dfs(head):
        if not head:
            return None, 0, None

        tail, counter, new_head = dfs(head.next)
        counter += 1
        current_node = ListNode(head.value)
        current_node.next = tail
        if counter == k:
            return current_node, counter, current_node
        return current_node, counter, new_head

    _, _, head = dfs(head)

    return head


# Test Cases
test.startProblem("1. Copy Kth")
LL1 = ListNode(13, ListNode(1, ListNode(
    5, ListNode(3, ListNode(7, ListNode(10))))))
test.test([10], arrayify(copyKthToLast(LL1, 1)), 1)
test.test([3, 7, 10], arrayify(copyKthToLast(LL1, 3)), 2)
test.test([13, 1, 5, 3, 7, 10], arrayify(copyKthToLast(LL1, 6)), 3)
test.test([], arrayify(copyKthToLast(LL1, 7)), 4)
test.endProblem()

################################################################################
# 2. Find the min element in an unsorted linked list (iterative)
#
# Q. Given an unsorted linked list, find the element with the lowest value.
#    Note: You must return the value of the max element not the element itself.
#
################################################################################


def findMin(head: ListNode) -> int:
    # Write your code here.
    def dfs(head, minVal):
        if not head:
            return minVal

        if head.value < minVal:
            return dfs(head.next, head.value)
        else:
            return dfs(head.next, minVal)

    return dfs(head, float('inf'))


# Test Cases
test.startProblem("2. Find Min Element")
LL1 = ListNode(1, ListNode(-4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
test.test(-4, findMin(LL1), 1)
test.test(1, findMin(LL2), 2)
test.test(-11, findMin(LL3), 3)
test.test(1, findMin(ListNode(1)), 4)
test.endProblem()

################################################################################
# 3. Bubble Sort (Sort odds)
# Q. Given an array of intgers, move all odd numbers to the left
#    in the order they appear.
#    Note: You may assume all values are positive integers.
#
# Example:
#     [3, 1, 4, 11, 2, 5] -> [3, 1, 11, 5, 4, 2]
#
################################################################################


def bubbleSortOdds(array: [int]) -> [int]:
    def is_odd(val):
        return val % 2 == 1
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if is_odd(array[j]) < is_odd(array[j+1]):
                array[j+1], array[j] = array[j], array[j+1]

    return array


# Test Cases
test.startProblem("3. Bubble Sort: Odds")
test.test([3, 1, 11, 5, 4, 2], bubbleSortOdds([3, 1, 4, 11, 2, 5]), 1)
test.test([1, 3, 13, 9, 5, 10, 8, 32], bubbleSortOdds(
    [10, 1, 3, 8, 13, 32, 9, 5]), 2)
test.endProblem()

################################################################################
# 4. Count unique elements in a binary tree (iterative and recursive)
#
# Q. Given a binary tree, count the numbers of unique elements.
#    in the tree.
#
################################################################################


def countTreeNodesIterative(root: TreeNode) -> int:
    if not root:
        return 0
    # Write your code here.
    counter = 0
    q = [root]
    nums = {}
    while q:
        node = q.pop()
        new_count = nums.get(node.value, 0) + 1
        if new_count == 1:
            counter += 1
        nums[node.value] = new_count
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return counter


def countTreeNodesRecursive(root: TreeNode) -> int:
    # Write your code here.
    nums = {}
    counter = 0

    def dfs(root):
        nonlocal counter
        if not root:
            return 0

        new_count = nums.get(root.value, 0) + 1
        if new_count == 1:
            counter += 1
        nums[root.value] = new_count
        dfs(root.left)
        dfs(root.right)

    dfs(root)

    return counter


# Test Cases
test.startProblem("4. Count Unique Tree Nodes")
test.test(0, countTreeNodesIterative(None), 1)
test.test(3, countTreeNodesIterative(
    TreeNode(1, TreeNode(-2), TreeNode(0))), 2)
test.test(4, countTreeNodesIterative(TreeNode(-2, TreeNode(-2,
          TreeNode(26)), TreeNode(2, None, TreeNode(2, TreeNode(-9))))), 3)
test.test(1, countTreeNodesIterative(TreeNode()), 4)
test.test(1, countTreeNodesIterative(TreeNode(-1)), 5)
test.test(0, countTreeNodesRecursive(None), 6)
test.test(3, countTreeNodesRecursive(
    TreeNode(1, TreeNode(-2), TreeNode(0))), 7)
test.test(4, countTreeNodesRecursive(TreeNode(-2, TreeNode(-2,
          TreeNode(26)), TreeNode(2, None, TreeNode(2, TreeNode(-9))))), 8)
test.test(1, countTreeNodesRecursive(TreeNode()), 9)
test.test(1, countTreeNodesRecursive(TreeNode(-1)), 10)
test.endProblem()

################################################################################

test.printFinal()
