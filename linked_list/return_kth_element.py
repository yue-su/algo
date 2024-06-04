class Node:
    def __init__(self, value, next=None):
       self.val = value
       self.next = next

def everyKthNode(node: Node, target: int) -> Node:

    index = 0
    dummy = Node(-1)
    p = dummy

    def helper(node):
        nonlocal index
        nonlocal p
        if node is None:
            return

        index += 1
        if index % target == 0:
            p.next = Node(node.val)
            p = p.next

        helper(node.next)
       
    helper(node)

    return dummy.next
          

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next
  return " -> ".join(parts)


# 1 -> 3 -> 6 -> 2 -> 8 -> 9
head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))

print(toString(everyKthNode(head, 3)))
print(toString(everyKthNode(head, 3)) == "6 -> 9")
print(toString(everyKthNode(head, 1)) == "1 -> 3 -> 6 -> 2 -> 8 -> 9")
print(toString(everyKthNode(head, 5)))
print(toString(everyKthNode(head, 5)) == "8")
print(toString(everyKthNode(head, 6)) == "9")
print(toString(everyKthNode(head, 7)) == "<empty>")

# 6
head = Node(6)
print(toString(everyKthNode(head, 1)) == "6")
print(toString(everyKthNode(head, 20)) == "<empty>")

# 6 -> 12
head = Node(6, Node(12))
print(toString(everyKthNode(head, 1)) == "6 -> 12")
print(toString(everyKthNode(head, 2)) == "12")

print(toString(everyKthNode(None, 5)) == "<empty>")