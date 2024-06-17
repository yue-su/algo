def first_k_times(input: list[int], k: int) -> int:
    nums = {}
    for num in input:
        count = nums.get(num, 0) + 1
        if count == k:
            return num
        nums[num] = count

    return -1


# Test Cases
print(first_k_times([1, 2, 2, 3, 3], 2))  # 2
print(first_k_times([1, 2, 2, 3, 3], 3))  # -1
print(first_k_times([], 1))  # -1
