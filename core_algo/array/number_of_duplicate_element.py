def num_duplicates(array: list[int]) -> int:
    # Write your code here.
    if len(array) <= 1:
        return 0

    nums = {}
    counter = 0

    for num in array:
        new_count = nums.get(num, 0) + 1
        if new_count == 1:
            counter += 1
        if new_count == 2:
            counter -= 1
        nums[num] = new_count

    return counter


# Test Cases
print(num_duplicates([]))  # 0
print(num_duplicates([3, 1, 1, 2, 3, 1, 1, 1, 4]))  # 2
print(num_duplicates([1]))  # 0
