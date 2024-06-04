
def subsets(nums: list[int]) -> list[list[int]]:
    track = []
    res = []

    def helper(start):
     
        res.append(track.copy())

        for i in range(start, len(nums)):

            track.append(nums[i])
            helper(i + 1)
            track.pop()

    helper(0)

    return res
    

print(subsets([1,2,3]))
