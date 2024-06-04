
'''
❓ PROMPT
Given a linked list and a positive number, *k*, reverse *k* items in the list at a time and reverse the remaining fragment if any.

Example(s)
head = 1 -> 2 -> 3
reverseBlocks(head, 2) == "2 -> 1 -> 3"

head = 1 -> 2 -> 3 -> 4 -> 5 -> 6
reverseBlocks(head, 3) == "3 -> 2 -> 1 -> 6 -> 5 -> 4"
 

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
function reverseBlocks(head, k) {
def reverseBlocks(head: Node, k: int) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def reverseBlocks(head: Node, k: int) -> Node:
  pass
  


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

print(toString(reverseBlocks(None, 1)) == "<empty>")

head = Node(1) # 1
print(toString(reverseBlocks(head, 1)) == "1")

head = Node(1) # 1
print(toString(reverseBlocks(head, 9)) == "1")

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(toString(reverseBlocks(head, 1)) == "1 -> 2 -> 3")

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(toString(reverseBlocks(head, 2)) == "2 -> 1 -> 3")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 3)) == "3 -> 2 -> 1 -> 6 -> 5 -> 4")

# 5 -> 6 -> 9
head = Node(5, Node(6, Node(9)))
print(toString(reverseBlocks(head, 3)) == "9 -> 6 -> 5")

# 2 -> 2 -> 2
head = Node(2, Node(2, Node(2)))
print(toString(reverseBlocks(head, 2)) == "2 -> 2 -> 2")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 2)) == "2 -> 1 -> 4 -> 3 -> 6 -> 5")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 4)) == "4 -> 3 -> 2 -> 1 -> 6 -> 5")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 5)) == "5 -> 4 -> 3 -> 2 -> 1 -> 6")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 5)) == "5 -> 4 -> 3 -> 2 -> 1 -> 6")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 6)) == "6 -> 5 -> 4 -> 3 -> 2 -> 1")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 9)) == "6 -> 5 -> 4 -> 3 -> 2 -> 1")