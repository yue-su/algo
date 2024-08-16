'''
Q1:

Given an array of integers, find a contiguous subarray which has the largest sum.
The subarray should contain at least one number.
Example

Example 1:
Input:
nums = [-2,2,-3,4,-1,2,1,-5,3]
Output:
6
Explanation:
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Example 2:
Input:
nums = [1,2,3,4]
Output:
10
Explanation:
the contiguous subarray [1,2,3,4] has the largest sum = 10.
'''


def find(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for p in range(1, len(nums)):
        current_sum = max(nums[p], current_sum + nums[p])
        max_sum = max(max_sum, current_sum)

    return max_sum


print(find([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
print(find([-2, 2, -3]))
print(find([1, 2, 3, 4]))
print(find([-1, -2, 3, 4]))
