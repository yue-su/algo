from test_case import Test
# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# ✏️ Description
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
# Q. Given a string, find the longest palindromic substring. You may assume there is only one longest substring.

# Examples:
# • Given a string: "babe" // returns"bab"
# • Given a string: "aefez" // returns "efe"

# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# 🟦 Python
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔




def lps2(input: str) -> str:
    # Write your code here.

    def is_panlindrom(left, right):
        while left <= right:
            if input[left] != input[right]:
                return False
            left += 1
            right -= 1
        return True

    res = ""
    max_length = 0

    def helper(start):
        nonlocal res
        nonlocal max_length

        if start == len(input):
            return

        for i in range(start, len(input)):
            if is_panlindrom(start, i):
                if i + 1 - start > max_length:
                    max_length = i + 1 - start
                    res = input[start: i+1]
            helper(i+1)

    helper(0)
    return res


def lps(input: str) -> str:

    max_length = 0
    start, end = 0, 0

    def find_longest(left, right):
        nonlocal start, end
        nonlocal max_length
        while left >= 0 and right <= len(input)-1 and input[left] == input[right]:
            if right + 1 - left > max_length:
                max_length = right - left
                start = left
                end = right
            left -= 1
            right += 1

    for index in range(len(input)):
        find_longest(index, index)
        find_longest(index, index + 1)

    return input[start:end+1]


test = Test()


# Test Cases
test.startProblem("Longest Palindromic Substring")
test.test("bab", lps("babe"), 1)
test.test("xyzzyx", lps("abaxyzzyxf"), 2)
test.test("noon", lps("it's afternoon"), 3)
test.test("a", lps("a"), 4)
test.test("b12365456321b", lps("kb12365456321bb"), 5)
test.endProblem()
