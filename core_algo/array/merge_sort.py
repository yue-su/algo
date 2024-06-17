def merge_sort(array: list[int]) -> list[int]:
    # Write your code here.
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    p1 = p2 = 0
    res = []
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    res += left[p1:]
    res += right[p2:]

    return res


# Test Cases
print(merge_sort([]))  # []
print(merge_sort([1]))  # [1]
print(merge_sort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(merge_sort([-10, 1, 3, 8, -13, 32, 9, 5]))
print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))
