def bubble_sort(array: list[int]) -> [int]:
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


# Test Cases
print(bubble_sort([]))  # []
print(bubble_sort([1]))  # [1]
print(bubble_sort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(bubble_sort([-10, 1, 3, 8, -13, 32, 9, 5]))
