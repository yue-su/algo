'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Implement the following operations of a stack using queues:
     • push(x): Push element x onto stack.
     • pop(): Removes the element on top of the stack.
     • top(): Get the top element.
     • empty(): Return whether the stack is empty.

Note: 
• You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
• Depending on your language, queue may not be supported natively.
• You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
• You may assume that all operations are valid (e.g. no pop or top operations will be called on an empty stack).

Examples:
//     stack = MyStack()
//     stack.push(3)
//     stack.push(7)
//     stack.top()        // returns 7
//     stack.pop()        // returns 7
//     stack.isEmpty()    // returns False
//     stack.top()        // returns 3
//     stack.pop()        // returns 3
//     stack.isEmpty()    // returns True
'''

'''
a) using two queues
b) swap the data and cache's reference instead of moving data back and forth

'''

from test_case import Test


class MyStack:
    # Write your code here.

    def __init__(self):
        # Write your code here.
        self.data = []
        self.cache = []

    # Push element x onto stack.
    def push(self, x: int) -> None:
        # Write your code here.
        self.cache.append(x)
        while self.data:
            self.cache.append(self.data.pop(0))
        self.data, self.cache = self.cache, self.data

    # Removes the element on top of the stack and returns that element.
    def pop(self) -> int:
        # Write your code here.
        return self.data.pop(0)

    # Get the top element
    def top(self) -> int:
        # Write your code here.
        return self.data[0]

    # Returns whether the stack is empty.
    def isEmpty(self) -> bool:
        # Write your code here.
        return len(self.data) == 0


test = Test("")

# Test Cases
test.startProblem("Implement Stack Using Queues")
stack1 = MyStack()
test.test(True, stack1.isEmpty(), 1)
stack1.push(1)
test.test(1, stack1.top(), 2)
stack1.push(2)
test.test(2, stack1.top(), 3)
test.test(2, stack1.pop(), 4)
test.test(False, stack1.isEmpty(), 5)
test.test(1, stack1.pop(), 6)
test.test(True, stack1.isEmpty(), 7)
test.endProblem()
