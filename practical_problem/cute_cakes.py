/*
'''
At a large party, we have many cakes of various sizes. We want to give all of the attendees the largest possible slice we can, but also make sure all of the slices are the same size. 
The cakes are all long and rectangular, therefore each cake is represented by a single number indicating it's length.

Given an array of cake sizes and number of attendees, what is the largest piece of cake we can give each person. We want to give each person one whole piece of cake, not two that add up to the given size. Any leftover portions of cake can be used to make cake pops!
 

EXAMPLE(S)
For cakes [5, 2, 7, 6, 9] and 5 attendees, the largest slice we can cut is 4.
- We can cut one slice of size 4 from the first cake with some leftover.
- We don't use the second cake.
- We can get one slice out of the third and fourth cakes.
- The final cake of size 9, we can cut two slices.
- If we tried to cut slices of size 5, we can only make three from the cakes of length 5, 7, and 9 so 4 is the best we can do.

For cakes [1, 2, 3, 4, 9] and 6 attendees, the largest slice we can cut is 2.
- We can't use the first cake, but can get one slice out of the next 2.
- The cake of size four we can divide in half to get two slices.
- We can get four slices out of the cake of length 9.
 

FUNCTION SIGNATURE
function maxSliceSize(cakes, attendees)
def max_slice_size(cakes, attendees):
'''
'''
bruteforce solution:
1. sort the cakes array
2. set the initial slice size to cakes[0]
3. loop through the cakes array and find out how many slices we can have.
4. increment the slice size 1 for each loop
5. stop when the slices == attendees
6. return slices

O(NlogC) + O(NlogN) =
O(NlogC) + O(N)

console.log(maxLength([5, 2, 7, 4, 9], 5), 4)
console.log(maxLength([1, 2, 3, 4, 9], 6), 2)
console.log(maxLength([1, 2, 3, 4, 9], 5), 3)
console.log(maxLength([8, 4, 2, 6, 1, 2, 1, 7], 14), 2)
console.log(maxLength([4, 9, 4, 3, 6, 6, 2, 5, 8, 7, 6], 13), 3)
console.log(maxLength([5, 4], 10), 0)

print(maxSliceSize([5, 2, 7, 4, 9], 5))  # Output: 4
print(maxSliceSize([1, 2, 3, 4, 9], 6))  # Output: 2
print(maxSliceSize([1, 2, 3, 4, 9], 5))  # Output: 3
print(maxSliceSize([8, 4, 2, 6, 1, 2, 1, 7], 14))  # Output: 2
print(maxSliceSize([4, 9, 4, 3, 6, 6, 2, 5, 8, 7, 6], 13))  # Output: 3
print(maxSliceSize([5, 4], 10))  # Output: 0
*/
'''


def max_slice_size(cakes, attendees):
  right = max(cakes)
  left = 1

  while left <= right:
    mid = left + (right - left) // 2
    slices = 0
    for cake in cakes:
      slices += cake // mid
    if slices < attendees:
      right = mid - 1
    else:
      left = mid + 1

  return right


print(max_slice_size([5, 2, 7, 4, 9], 5))  # Output: 4
print(max_slice_size([1, 2, 3, 4, 9], 6))  # Output: 2
print(max_slice_size([1, 2, 3, 4, 9], 5))  # Output: 3
print(max_slice_size([8, 4, 2, 6, 1, 2, 1, 7], 14))  # Output: 2
print(max_slice_size([4, 9, 4, 3, 6, 6, 2, 5, 8, 7, 6], 13))  # Output: 3
print(max_slice_size([5, 4], 10))  # Output: 0
