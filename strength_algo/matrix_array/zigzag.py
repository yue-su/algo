
from typing import List


def zigZag(n: int, arr: List[int]) -> None:
    p = 0
    flag = True

    while p < len(arr) - 1:
        if flag:
            if arr[p] > arr[p+1]:
                arr[p], arr[p+1] = arr[p+1], arr[p]
        else:
            if arr[p] < arr[p+1]:
                arr[p], arr[p+1] = arr[p+1], arr[p]
        flag = not flag
        p += 1

    return arr


print(zigZag(7, [4, 3, 7, 8, 6, 2, 1]))
