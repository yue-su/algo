'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of integers, find all unique triplets (a, b, c) in the array such that their sum equals zero (a + b + c = 0).

Examples:
• Given an array: [1, 2, 0] returns: []
• Given an array: [-1, 0, 1, 0, 1] returns: [[-1, 0, 1]]
• Given an array: [-5, -1, 0, 1, 4, -1] returns: [[-5,1,4], [-1,0,1]]

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def tns(input) -> [[int]]:
    # Write your code here.
    return []

# Test Cases
test.startProblem("Three Number Sum")
test.test([], tns([]), 1)
test.test([[-1, 0, 1]], tns([-1, 0, 1]), 2)
test.test([[-1, 0, 1]], tns([-1, -1, 1, 1, 0, 0]), 3)
test.testMatchAny([[-1, 0, 1], [-5, 1, 4]], tns([-5, -1, 0, 1, 4, -1]), 4)
test.endProblem()
'''

from test_case import Test


def tns(input: [int]) -> [[int]]:
    if not input:
        return []

    track = []
    res = []
    used = [False]*len(input)
    sums = 0

    input.sort()

    def helper(start):
        nonlocal sums
        if sums == 0 and len(track) == 3:
            res.append(track.copy())
            return

        for i in range(start, len(input)):
            if i > 0 and input[i] == input[i - 1] and not used[i-1]:
                continue

            track.append(input[i])
            sums += input[i]
            used[i] = True
            helper(i + 1)
            used[i] = False
            track.pop()
            sums -= input[i]

    helper(0)

    return res


test = Test("")

test.startProblem("Three Number Sum")
test.test([], tns([]), 1)
test.test([[-1, 0, 1]], tns([-1, 0, 1]), 2)
test.test([[-1, 0, 1]], tns([-1, -1, 1, 1, 0, 0]), 3)
test.testMatchAny([[-1, 0, 1], [-5, 1, 4]], tns([-5, -1, 0, 1, 4, -1]), 4)
test.endProblem()
