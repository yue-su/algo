def getAllSubsequences1(word: str) -> list[str]:
    res = []

    if len(word) == 0:
        return res

    def helper(word, sub):
        if len(word) == 0:
            if len(sub) > 0:
                res.append(sub)
            return

        helper(word[1:], sub)
        helper(word[1:], sub + word[0])

    helper(word, "")

    return res


def getAllSubsequences(word):
    res = []
    track = []

    if not word:
        return res

    def helper(start):
        if track:
            res.append("".join(track))

        for i in range(start, len(word)):
            track.append(word[i])
            helper(i + 1)
            track.pop()

    helper(0)

    return res



print(getAllSubsequences("abc"))
# use a set for results to make them order agnostic
print(getAllSubsequences("") == [])
print(getAllSubsequences("a") == ["a"])
print(set(getAllSubsequences("ab")) == set(["b", "a", "ab"]))
print(set(getAllSubsequences("abc")) == set(
    ["c", "b", "bc", "a", "ac", "ab", "abc"]))
print(set(getAllSubsequences("abcd")) == set(
    ["d", "c", "cd", "b", "bd", "bc", "bcd", "a", "ad", "ac", "acd", "ab", "abd", "abc", "abcd"]))
print(set(getAllSubsequences("1A")) == set(["A", "1", "1A"]))
print(set(getAllSubsequences("1A2b")) == set(
    ["b", "2", "2b", "A", "Ab", "A2", "A2b", "1", "1b", "12", "12b", "1A", "1Ab", "1A2", "1A2b"]))
print(len(getAllSubsequences("jesitony")) == 255)
