def fourSum(nums: list[int], target: int):
    nums.sort()
    print(nums)
    pairs_map = {}
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i + 1, n):
            pairs_map[(i, j)] = nums[i] + nums[j]

    value_indexs = [[pairs_map[key], key] for key in pairs_map]
    value_indexs.sort()

    left = 0
    right = len(value_indexs) - 1

    print(value_indexs)

    while left < right:
        if value_indexs[left][0] + value_indexs[right][0] == target:
            indexes = value_indexs[left][1] + value_indexs[right][1]
            values = [nums[index] for index in indexes]
            
            res.add(tuple(values))
            right -= 1
            left += 1
        elif value_indexs[left][0] + value_indexs[right][0] > target:
            right -= 1
        else:
            left += 1

    print(res)
    return res


# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
fourSum([1, 0, -1, 0, -2, 2], 0)
# fourSum([2, 2, 2, 2, 2], 0)
