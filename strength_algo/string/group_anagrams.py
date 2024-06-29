# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# ✏️ Description
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
# Q. Given an array of strings, group anagrams together.

# Note:
# • Anagrams are strings fromed by rearranging the letters of a different word or phrase. (e.g. LISTEN < -> SILENT, a < -> a)

# Examples:
# • Given array: ["cat", "act", "a", "tac"] // returns[["a"], ["act", "cat", "tac"]]
# • Given array:  array: ["a", "ab", "ba"] // returns[["a"], ["ab", "ba"]]

# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# 🟦 Python
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔


from test_case import Test


def ga(strs: list[str]) -> list[list[str]]:
    # Write your code here.
    sorted_map = {}

    for str in strs:
        sorted_str = ''.join(sorted(str))
        if sorted_str in sorted_map:
            sorted_map[sorted_str] += [str]
        else:
            sorted_map[sorted_str] = [str]

    return [value for value in sorted_map.values()]


print(ga(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


test = Test()

# Test Cases
test.startProblem("Group Anagrams:")
test.testMatchAny([["foo"], ["oy", "yo"], ["tac", "cat", "act"], ["flop", "olfp"]], ga(
    ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]), 1)
test.testMatchAny([["a"], ["act", "cat", "tac"]],
                  ga(["cat", "act", "a", "tac"]), 2)
test.testMatchAny([["a"], ["ab", "ba"]], ga(["a", "ab", "ba"]), 3)
test.testMatchAny([], ga([]), 4)
test.testMatchAny([["Formation"]], ga(["Formation"]), 5)
test.endProblem()
