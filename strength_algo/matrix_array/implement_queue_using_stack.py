from test_case import Test


class MyQueue:
    # Write your code here.

    # Initialize your data structure here.
    def __init__(self):
        # Write your code here.
        pass

    # Push element x to the back of queue.
    def push(self, x: int) -> None:
        # Write your code here.
        pass

    # Removes the element from in front of queue and returns that element.
    def pop(self) -> int:
        # Write your code here.
        pass

    # Get the front element.
    def peek(self) -> int:
        # Write your code here.
        pass

    # Returns whether the queue is empty.
    def isEmpty(self) -> bool:
        # Write your code here.
        pass


test = Test("")
# Test Cases
test.startProblem("Implement Queue Using Stacks")
queue1 = MyQueue()
test.test(True, queue1.isEmpty(), 1)
queue1.push(1)
test.test(1, queue1.peek(), 2)
queue1.push(2)
test.test(1, queue1.peek(), 3)
test.test(1, queue1.pop(), 4)
test.test(2, queue1.peek(), 5)
test.test(False, queue1.isEmpty(), 6)
test.test(2, queue1.pop(), 7)
test.test(True, queue1.isEmpty(), 8)
test.endProblem()
