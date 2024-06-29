""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a string, return the index of the first occurrence of a target string. Return - 1 if the input string does not contain the target string.

Examples:
• Given a string: "hello", target: "ll" // returns 2
• Given a string: "formation", target: "afor" // returns - 1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ """


from test_case import Test


def strStr(inputString: str, target: str) -> int:

    def is_match(index, start):

        if start == len(target):
            return True

        if inputString[index] != target[start]:
            return False

        return is_match(index + 1, start + 1)

    for i in range(len(inputString)):
        if is_match(i, 0):
            return i

    return -1


test = Test()


# Test Cases
test.startProblem("Implement strStr")
test.test(2, strStr("hello", "ll"), 1)
test.test(-1, strStr("", "a"), 2)
test.test(0, strStr("aaaaaaa", "a"), 3)
test.test(-1, strStr("formation", "afor"), 4)
test.test(-1, strStr("formation", "fora"), 5)
test.endProblem()
