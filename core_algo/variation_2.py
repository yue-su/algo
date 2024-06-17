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


test = Test("Core Algos — Variation Set #2")


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
# 1. 1/3 of the Linked List
#
# Q. Given a linked list, return the value of the element that is at the 1/3 position.
#    Note: You may assume the total number of elements is multiples of 3.
#          (e.g. 3, 6, 9, 12 ...)
#
# Example:
#     Given a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6   // returns 2
#
################################################################################


def findOneThirdElement2(head: ListNode) -> int:
    # Write your code here.
    def dfs(head, l):
        if not head:
            return l, 0, -1

        l += 1
        total_length, counter, value = dfs(head.next, l)
        counter += 1
        if counter == total_length * 2 // 3 + 1:
            return total_length, counter, head.value

        return total_length, counter, value

    _, _, res = dfs(head, 0)
    print(res)
    return res


def findOneThirdElement(head: ListNode) -> int:
    fast = slow = head
    while fast.next and fast.next.next and fast.next.next.next:
        slow = slow.next
        fast = fast.next.next.next

    return slow.value


# Test Cases
LL5 = ListNode(1, ListNode(2, ListNode(3)))
LL6 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))
test.startProblem("1. Find 1/3 Position")
test.test(1, findOneThirdElement(LL5), 1)
test.test(2, findOneThirdElement(LL6), 2)
test.endProblem()

################################################################################
# 2. Find the most repeated element in a linked list
#
# Q. Given an unsorted array with possible duplicate element values,
#    return the most repeated element's value.
#    Note: - You must return the integer value not the node itself.
#          - You must assume there is only one value repeated the most.
#
# Examples:
#   Input:  1->2->1->1->2->3->3->3->3
#   Output: 3 (4 times)
#
################################################################################


def findMostRepeated(head: ListNode) -> int:
    # Write your code here.
    nums = {}
    max_count = 0
    res = 0
    while head:
        new_count = nums.get(head.value, 0) + 1
        if new_count > max_count:
            max_count = new_count
            res = head.value
        nums[head.value] = new_count
        head = head.next

    return res


# Test Cases
test.startProblem("2. Find Most Repeated")
LL1 = ListNode(1, ListNode(3, ListNode(5, ListNode(1))))
LL2 = ListNode(1, ListNode(2, ListNode(1, ListNode(1, ListNode(
    2, ListNode(3, ListNode(3, ListNode(3, ListNode(3)))))))))
test.test(1, findMostRepeated(LL1), 1)
test.test(3, findMostRepeated(LL2), 2)
test.test(7, findMostRepeated(ListNode(7)), 3)
test.endProblem()

################################################################################
# 3. Binary Search (with duplicates)
#
# Q. Given a sorted array of n integers and a target integer, check
#    if the array contains a target via binary search.
#    Note: You must return whether it contains the target or not (boolean).
#
################################################################################


def binarySearch(array: [int], target: int) -> bool:
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


# Test Cases
test.startProblem("3. Binary Search")
array = [1, 2, 3, 3, 3, 6, 8, 13, 13, 113, 153, 200]
test.test(True, binarySearch(array, 1), 1)
test.test(True, binarySearch(array, 200), 2)
test.test(True, binarySearch(array, 3), 3)
test.test(False, binarySearch(array, 154), 4)
test.endProblem()

################################################################################
# 4. Count negative elements in a binary tree (iterative and recursive)
#
# Q. Given a binary tree, count the number of elements with negative values
#    in the tree.
#    Note: 0 is non-negative integer.
#
################################################################################


def countTreeNodesIterative(root: TreeNode) -> int:
    # Write your code here.
    pass


def countTreeNodesRecursive(root: TreeNode) -> int:
    # Write your code here.
    pass


# Test Cases
test.startProblem("4. Count Negative Tree Nodes")
test.test(0, countTreeNodesIterative(None), 1)
test.test(1, countTreeNodesIterative(
    TreeNode(1, TreeNode(-2), TreeNode(0))), 2)
test.test(2, countTreeNodesIterative(TreeNode(-2, TreeNode(29,
          TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(-9))))), 3)
test.test(0, countTreeNodesIterative(TreeNode()), 4)
test.test(1, countTreeNodesIterative(TreeNode(-1)), 5)
test.test(0, countTreeNodesRecursive(None), 6)
test.test(1, countTreeNodesRecursive(
    TreeNode(1, TreeNode(-2), TreeNode(0))), 7)
test.test(2, countTreeNodesRecursive(TreeNode(-2, TreeNode(29,
          TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(-9))))), 8)
test.test(0, countTreeNodesRecursive(TreeNode()), 9)
test.test(1, countTreeNodesRecursive(TreeNode(-1)), 5)
test.endProblem()

################################################################################

test.printFinal()
