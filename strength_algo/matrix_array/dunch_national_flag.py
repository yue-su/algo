'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of 0s, 1s, and 2s, sort them in-place in ascending order.

Examples:
• Given an array: [2, 1] // returns [1, 2]
• Given an array: [0, 2, 1, 0, 1, 2] // returns [0, 0, 1, 1, 2, 2]

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def dnf(input: [int]) -> None:
    # Write your code here.
    pass

# Test Cases
test.startProblem("Dutch National Flag")
array1 = []; dnf(array1)
array2 = [2, 1, 1, 0]; dnf(array2)
array3 = [0, 2, 1, 0, 1, 2]; dnf(array3)
test.test([], array1, 1)
test.test([0, 1, 1, 2], array2, 2)
test.test([0, 0, 1, 1, 2, 2], array3, 3)
test.endProblem()
'''


def dnf(input: [int]) -> None:
    if not input:
        return

    left = 0
    right = len(input) - 1
    p = 0

    # p need to check the last right because the right has not been checked
    while p <= right:
        if input[p] == 0:
            input[p], input[left] = input[left], input[p]
            left += 1
            p += 1  # we know the current left can only be 1 or 0 so we increment p

        elif input[p] == 2:
            input[p], input[right] = input[right], input[p]
            right -= 1
            # after the swap, we don't know the current p is 0, 1 or 2, so do not increment p

        else:
            # if it is a 1, go to the next
            p += 1

    return


array1 = [2, 1, 1, 0]
array2 = [2, 1, 0, 0, 1, 1, 0, 1, 2, 2, 0, 1]
dnf(array1)
print(array1)
dnf(array2)
print(array2)


def dnf2(input: [int]) -> None:
    if not input:
        return

    for i in range(len(input) - 1):
        for j in range(len(input)-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]

    return
