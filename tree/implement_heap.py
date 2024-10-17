
'''
A priority queue is a data structure that allows inserting and removing data elements one at a time, keeps that data organized, and the removals are prioritized by some criteria: either the smallest current value first (as in a min heap), the largest (a max heap), or some other method of comparing and ordering the removals.

A heap is a specific way of implementing a priority queue. The key idea is to use an array, organized as a complete tree. Recall that a complete tree is one where every level except the last is full, and the last incomplete level has all of the nodes pushed to the left.

Being a complete tree, this can be implemented as an array:
- The root of the tree is at index zero.
- Given an index:

  - The left child is at (index * 2) + 1
  - The right child is at (index * 2) + 2
  - These can be reversed to compute a parent index

For this problem, start out building a Min Heap, that is, a heap where the smallest values bubble to the top and are removed first. As a follow on, you can modify this code to take a comparator function as a parameter to the constructor, allowing it to be a min or max heap.
 

EXAMPLE(S)
const h = new Heap(10);
h.peek() => undefined
h.add(3);
h.peek() => 3
h.add(2);
h.peek() => 2
h.remove() => 2
h.peek() => 3
h.add(4);
h.add(1);
h.add(5);
h.remove() => 1
 

FUNCTION SIGNATURE
class Heap {

  constructor(capacity, comparator)
    - initialize an array with capacity (none or undefined)
    - comparator will be default for min heap (lambda: a > b)
    - initialize length to 0  

  add(value)


  remove()
    - remember the value to be removed (index 0)
    - copy the last value of the heap into position of index 0 
    - replace the value in the last position (now duplicated) with an undefined or none.
    - decrement the length by 1 
    - value at top (which we just replaced) needs to be bubbled down 
      - if this value is bigger than any child, swap with that respective child 
      - keep repeating this step until no swaps needed     
    - at the end, return the remembered value from step 1 

  peek()
    - return first position of array
    // length should be available as the number of elements currently in the heap
}
'''


class Heap:
    def __init__(self, capacity, comparator=None):
        self.data = [None] * capacity
        self.length = 0
        self.comparator = comparator or (lambda a, b: a > b)

    """
    add():
        If there isn't enough room in the array, push an undefined or None
        Place the new value at the position of length and remember this index.
        Increment the length counter.
        Now the new value needs to be bubbled UP in the heap if it meets the criteria (is smaller than it's parent for a min heap).
        As long as the value at the remembered position is smaller than it's parent, swap
        The new position is the position we swapped to.
    """

    def add(self, val):
        if self.length == len(self.data):
            self.data.append(None)
        curr = self.length
        self.data[curr] = val
        self.length += 1
        while curr > 0:
            p = self.parent(curr)
            pval, cval = self.data[p], self.data[curr]
            if self.comparator(pval, cval):
                self.data[p], self.data[curr] = cval, pval
                curr = p
            else:
                break

    """
    remove():
        Remember the value at the first (index 0) position in the heap.
        Copy the last value in the heap (position length - 1) into position 0.
        Replace the value in the last position (now duplicated) with an undefined or None.
        Decrement the length counter
        Now this value at the top needs to be bubbled DOWN to a new position (if it is larger than any of it's children)
        As long as the value is larger than any of it's current children, swap it with the smaller of the children.
        At the end, return the remembered value from the first step.
    """

    def remove(self):
        if self.length == 0:
            return None
        val = self.peek()
        self.length -= 1
        self.data[0], self.data[self.length] = self.data[self.length], None
        curr = 0
        while curr < self.length - 1:
            cval = self.data[curr]
            left, right = self.left(curr), self.right(curr)
            lval, rval = self.data[left], self.data[right]
            swapLeft = right >= self.length or self.comparator(rval, lval)
            go, val = (left, lval) if swapLeft else (right, rval)
            if self.comparator(cval, val):
                self.data[curr], self.data[go] = val, cval
                curr = go
            else:
                break
        return val

    def peek(self):
        return self.data[0] if self.length > 0 else None

    def parent(self, index):
        sub = 2 if index % 2 == 0 else 1
        return (index - sub) // 2

    def left(self, index):
        return index * 2 + 1

    def right(self, index):
        return index * 2 + 2
