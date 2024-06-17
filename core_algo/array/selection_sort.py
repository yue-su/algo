def selection_sort(array: list[int]) -> [int]:
    # Write your code here.
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


# Test Cases
print(selection_sort([]))  # []
print(selection_sort([1]))  # [1]
print(selection_sort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(selection_sort([-10, 1, 3, 8, -13, 32, 9, 5]))
