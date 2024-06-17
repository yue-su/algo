def num_uniques(array: list[int]) -> int:
    nums = {}
    for num in array:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

    return len([x for x in nums if nums[x] == 1])


# Test Cases
print(num_uniques([]))  # 0
print(num_uniques([3, 1, 1, 2, 3, 1, 1, 1, 4]))  # 2
print(num_uniques([1]))  # 1
