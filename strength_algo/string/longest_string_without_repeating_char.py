""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a string, return the longest substring witout repeating characters.

Examples:
• Given a string: "abcbde" // returns "cbde"
• Given a string: "abc" // returns "abc"

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
 """


from test_case import Test


def longestSubstringNoDupes(string: str) -> str:
    left = right = 0
    chars = set()
    max_length = 0
    start = end = 0

    while right < len(string):
        if string[right] not in chars:
            chars.add(string[right])
            if right - left > max_length:
                max_length = right - left
                start, end = left, right
            right += 1
        else:
            chars.remove(string[left])
            left += 1

    return string[start: end+1]


test = Test()

# Test Cases
test.startProblem("Longest Substring without Repeats")
test.test("a", longestSubstringNoDupes("a"), 1)
test.test("abc", longestSubstringNoDupes("abc"), 2)
test.test("cdea", longestSubstringNoDupes("abccdeaabbcddef"), 3)
test.test("cbde", longestSubstringNoDupes("abcbde"), 4)
test.test("bac", longestSubstringNoDupes("abacacacaaabacaaaeaaafa"), 5)
test.endProblem()
