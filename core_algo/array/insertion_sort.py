def insertion_sort(array: list[int]) -> [int]:
    # Write your code here.
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

    return array


# Test Cases
print(insertion_sort([]))  # []
print(insertion_sort([1]))  # [1]
print(insertion_sort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(insertion_sort([-10, 1, 3, 8, -13, 32, 9, 5]))
