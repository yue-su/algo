"""

Given a linked list representing an integer, write a function that adds one to this number.

Each node represents a digit, the most significant digit is at the head.

in: 1 -> 2 -> 3 -> null
// int => 123
out: 1 -> 2 -> 4 -> null
// int => 124


options

1. convert to int, increment, convert to LL               // O(N) time, O(1) / O(N) space
2. reverse LL, iterate over and increment, reverse again   // O(N) time, O(1) space
3. recursive post-order traversal while incrementing     // O(N) time, O(N) space

"""


class Node:
  def __init__(self, val: int, next=None) -> None:
    self.val = val
    self.next = next

  # turn the linked list into a string
  def __str__(self) -> str:
    curr = self
    string = ''

    while curr:
      string += str(curr.val)
      curr = curr.next

    return string


def addOne(head: Node) -> Node:
  dummy = Node(0)
  dummy.next = head
  p = dummy
  isCarry = False

  def helper(head):
    nonlocal isCarry

    if head.next is None:
      new_val = head.val + 1
      if new_val >= 10:
        isCarry = True
      head.val = new_val % 10
      return

    helper(head.next)
    if isCarry:
      new_val = head.val + 1
      if new_val < 10:
        isCarry = False
        head.val = new_val
      else:
        isCarry = True
        head.val = 0

  helper(p)

  if dummy.val == 0:
    return dummy.next
  else:
    return dummy


def addOneTwo(head: Node) -> Node:
  dummy = Node(0)
  dummy.next = head
  p = dummy

  def helper(head):

    if head.next is None:
      new_val = head.val + 1
      head.val = new_val % 10
      return True

    isCarry = helper(head.next)
    if isCarry:
      new_val = head.val + 1
      if new_val < 10:
        head.val = new_val
        return False
      else:
        head.val = 0
        return True

  helper(p)

  if dummy.val == 0:
    return dummy.next
  else:
    return dummy


int_999 = Node(9, Node(9, Node(9)))
int_1000 = Node(1, Node(0, Node(0, Node(0))))
int_123 = Node(1, Node(2, Node(3)))
int_124 = Node(1, Node(2, Node(4)))
int_9899 = Node(9, Node(8, Node(9, Node(9))))
int_9900 = Node(9, Node(9, Node(0, Node(0))))

print(str("0"))
print(str(addOne(Node(0))) == str(Node(1)))
print(str("999"))
print(str(addOne(int_999)) == str(int_1000))
print(str("123"))
print(str(addOne(int_123)) == str(int_124))
print(str("9899"))
print(str(addOne(int_9899)) == str(int_9900))
