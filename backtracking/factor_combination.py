class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def helper(n, start):
            res = []
            if n <= 3:
                return res

            for i in range(start, int(n ** 0.5) + 1):
                if n % i != 0:
                    continue

                res.append([i, n // i])
                sub_res = helper(n//i, i)
                for item in sub_res:
                    item.append(i)
                    res.append(item)

            return res
        return helper(n, 2)
