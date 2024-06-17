def binary_earch(array: list[int], target: int) -> int:
    # Write your code here.
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


# Test Cases
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binary_earch(array, 1))  # 0
print(binary_earch(array, 200))  # 8
print(binary_earch(array, 8))  # 4
print(binary_earch(array, 154))  # -1
