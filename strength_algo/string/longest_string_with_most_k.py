""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a string and a target k, return the longest substring with at most k characters.

Examples:
• Given a string = "aabbcc" & k = 1 // returns "aa"
• Given a string = "aabbcc" & k = 2 // returns "aabb"

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
 """


from test_case import Test


def longestSubstringWithDistinctKs(string, k):
    # Write your code here.
    left = 0
    right = 0
    chars = set()
    start = end = 0
    max_length = 0

    if not string or k == 0:
        return ""

    while right < len(string):
        while len(chars) <= k and right < len(string):
            chars.add(string[right])
            right += 1
            if len(chars) == k:
                if right - left > max_length:
                    max_length = right - left
                    start, end = left, right

        while len(chars) > k:
            left_char = string[left]
            chars.remove(left_char)
            while string[left] == left_char:
                left += 1

    if len(chars) < k:
        end = right

    return string[start: end]


def test_longestSubstringWithDistinctKs():
    assert longestSubstringWithDistinctKs(
        "abcabcbb", 2) == "bcbb", "Test case 1 failed"
    assert longestSubstringWithDistinctKs(
        "aaabbcc", 3) == "aaabbcc", "Test case 2 failed"
    assert longestSubstringWithDistinctKs(
        "aaabbcc", 10) == "aaabbcc", "Test case 3 failed"
    assert longestSubstringWithDistinctKs("", 3) == "", "Test case 4 failed"
    assert longestSubstringWithDistinctKs("a", 0) == "", "Test case 5 failed"
    assert longestSubstringWithDistinctKs("b", 1) == "b", "Test case 6 failed"
    assert longestSubstringWithDistinctKs(
        "aaaa", 1) == "aaaa", "Test case 7 failed"
    assert longestSubstringWithDistinctKs(
        "abcdef", 6) == "abcdef", "Test case 8 failed"
    assert longestSubstringWithDistinctKs(
        "aabbcc", 7) == "aabbcc", "Test case 9 failed"

    print("All test cases passed!")


test_longestSubstringWithDistinctKs()

test = Test()

# Test Cases
test.startProblem("Longest Substring with at most Ks")
test.test("aa", longestSubstringWithDistinctKs("aabbcc", 1), 1)
test.test("aabb", longestSubstringWithDistinctKs("aabbcc", 2), 2)
test.test("aabbcc", longestSubstringWithDistinctKs("aabbcc", 3), 3)
test.test("zbbcc", longestSubstringWithDistinctKs("azbbcc", 3), 4)
test.endProblem()
