class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        res = []

        def is_palindrome(sub):
            left = 0
            right = len(sub) - 1
            while left <= right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(start=0, track=[]):
            if start == len(s):
                res.append(track[:])
                return

            for i in range(start, len(s)):
                sub = s[start:i + 1]
                if not is_palindrome(sub):
                    continue
                track.append(sub)
                helper(i + 1, track)
                track.pop()

        helper()

        return res
