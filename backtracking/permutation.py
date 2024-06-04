class Solution:
    def permute(self, nums):
        res = []
        used = set()

        for num1 in nums:
            used.add(num1)
            for num2 in nums:
                if num2 not in used:
                    used.add(num2)
                    for num3 in nums:
                        if num3 not in used:
                            used.add(num3)
                            res.append([num1, num2, num3])
                            used.remove(num3)
                    used.remove(num2)
            used.remove(num1)

        return res
    
    def permute2(self, nums):

        res = []
        used = set()

        def helper(permutation):
            if len(used) == len(nums):
                res.append(permutation.copy())
                return
            
            for num in nums:
                if num in used:
                    continue

                used.add(num)
                permutation.append(num)
                helper(permutation)
                permutation.pop()
                used.remove(num)
        helper([])

        return res
             
            



test = Solution()
result = test.permute([1,2,3])
result2 = test.permute2([1,2,3,4])
print(result)
print(result2)
        