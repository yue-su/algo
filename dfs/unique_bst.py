class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(lo, hi):
            res = []
            if lo > hi:
                res.append(None)
                return res

            for i in range(lo, hi + 1):
                lefts = build(lo, i-1)
                rights = build(i+1, hi)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)

            return res

        return build(1, n)
