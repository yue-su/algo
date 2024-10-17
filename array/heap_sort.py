
'''
❓ PROMPT
** PART 1: Heapify *******************

An array can be used to represent a complete binary tree! Index 0 is the root, index 1 is the left child of the root, and index 2 is the right child! If there is a fourth value in the tree, it's now at index 3, beginning on the left, then the fifth is the right child. 

    1
  2   3
4  5

With this organization, given any index into the array, we can easily compute its parent and child indices. In this way we can move up and down the tree. What is the mathematical pattern here? For any index, what is the formula to obtain the index of the parent? The left and right children?

A max-heap is a binary tree that is not necessarily sorted, but every node's parent is greater than or equal to itself. If this property is true, then the largest value will be at the top (the root). A min-heap is the inverse: parent values are smaller than or equal and the smallest value is at the top.

The first part of this task is to take an array and re-arrange its elements so that it satisfies the requirements of a max-heap. One easy way out is to just sort the array, but that's not what we're looking for here.

** PART 2: Heap Sort *****************

Once we have an array that is heapified, it's not a big stretch to go from this point to fully sorted. Using your max-heap, heapify() implementation a first step, now finish sorting. How can this be done?

There is a good visualization for this on Wikipedia: https://en.wikipedia.org/wiki/Heapsort

Example(s)
heapify([0]) -> [0]
heapify([0, 1]) -> [1, 0]
heapify([1, 3, 2]) -> [3, 1, 2]

heapSort([0]) -> [0]
heapSort([1, 0]) -> [0, 1]
heapSort([1, 3, 2]) -> [1, 2, 3]
heapSort([5, 39, 23, 7, 52, 13]) -> [5, 7, 13, 23, 39, 52]

 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function heapify(array)
def heapify(array):

function heapSort(array)
def heap_sort(array):

While these two functions are the ones required by this task, feel free to write helper functions as needed and/or apprioriate!
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

https://labuladong.online/algo/data-structure-basic/binary-heap-implement/

'''

def heapify(array):
    def sift_down(i):
    
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < m and array[left] > array[largest]:
            largest = left

        # Check if right child exists and is greater than the current largest
        if right < m and array[right] > array[largest]:
            largest = right

        # If largest is not root, swap and continue to heapify
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            sift_down(largest)  # Recursively heapify the affected sub-tree

    m = len(array)

    # Edge case: Empty array or single element doesn't need heapifying
    if m < 2:
        return array

    # Start from the last non-leaf node and move upwards
    last_non_leaf = m // 2 - 1

    for i in range(last_non_leaf, -1, -1):
        sift_down(i)

    return array


print(heapify([0,1]))
print(heapify([3, 9, 2, 1, 4, 5]))
