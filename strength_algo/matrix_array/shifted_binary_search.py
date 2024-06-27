
'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a shifted sorted array of distinct integers and a target integer, determine if the array contains a target value by returning its index. Otherwise, return -1. Elements in the array are shifted by some amount (left or right).

Examples:
• Given an array: [6, 7, 1, 2, 3, 4, 5], target: 1 // returns: 2
• Given an array: [9, 15, 30, -33, 3, 7], target: 0 // returns: -1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def sbs(input: [int], target: int) -> int:
    # Write your code here.
    pass

# Test Cases
test.startProblem("Shifted Binary Search")
test.test(8, sbs([43, 51, 73, 78, 79, 0, 1, 3, 13, 35], 13), 1)
test.test(2, sbs([7, 26, 110, 2], 110), 2)
test.test(5, sbs([45, 60, 69, 74, 75, 0, 1, 3, 33, 39], 0), 3)
test.test(-1, sbs([30, 37, 44, 67, 68, 75, 77, 268, 0, 1, 19], 269), 4)
test.test(0, sbs([30, 37, 44, 67, 68, 75, 77, 268, 0, 1, 19], 30), 5)
test.endProblem()
'''

'''
a) first to find out whether the mid located in the left half or the right half
b) search in a sorted half
c) include the left and right when search
'''

from test_case import Test


def sbs(input: [int], target: int) -> int:
    # Write your code here.
    left, right = 0, len(input) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if input[mid] == target:
            return mid

        elif input[mid] > input[right]:
            if input[left] <= target < input[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if input[mid] < target <= input[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


test = Test("")

test.startProblem("Shifted Binary Search")
test.test(8, sbs([43, 51, 73, 78, 79, 0, 1, 3, 13, 35], 13), 1)
test.test(2, sbs([7, 26, 110, 2], 110), 2)
test.test(5, sbs([45, 60, 69, 74, 75, 0, 1, 3, 33, 39], 0), 3)
test.test(-1, sbs([30, 37, 44, 67, 68, 75, 77, 268, 0, 1, 19], 269), 4)
test.test(0, sbs([30, 37, 44, 67, 68, 75, 77, 268, 0, 1, 19], 30), 5)
test.endProblem()
