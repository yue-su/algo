
'''
❓ PROMPT
Given the head node of a singly linked list, remove all the nodes with values that appear more than once. Return the head node of the new linked list, after removing all the duplicate nodes.

Example(s)
head = 1->2->3
removeDuplicateNodes(head) == "1->2 ->3"

head = 6->4->8->3->4
removeDuplicateNodes(head) == "6->8->3"
 

🛠️ IMPLEMENT
function removeDuplicateNodes(head) {
def removeDuplicateNodes(head: Node) -> Node:
 
'''

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def removeDuplicateNodes(head: Node) -> Node:
    if not head:
       return None
    
    dummy = Node(-1)
    dummy.next = head
    p = dummy

    nums = {}

    while head:
        if head.val in nums:
            nums[head.val] += 1
        else:
            nums[head.val] = 1
        head = head.next
    
    while p and p.next:
        if nums[p.next.val] > 1:
            p.next = p.next.next
        else:
           p = p.next
            
    return dummy.next


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return "->".join(parts)

head = None
print(toString(removeDuplicateNodes(head)) == "<empty>")
 
 # 1
head = Node(1)
print(toString(removeDuplicateNodes(head)) == "1")
 
 # 1->1->2
head = Node(1, Node(1, Node(2)))
print(toString(removeDuplicateNodes(head)) == "2")
 
 # 1->2->3
head = Node(1, Node(2, Node(3)))
print(toString(removeDuplicateNodes(head)) == "1->2->3")
 
 # 6->4->8->3->4
head = Node(6, Node(4, Node(8, Node(3, Node(4))))) 
print(toString(removeDuplicateNodes(head)) == "6->8->3")
 
 # 4->3->4->1->5
head = Node(4, Node(3, Node(4, Node(1, Node(5)))))
print(toString(removeDuplicateNodes(head)) == "3->1->5")
 
 # 4->3->4->1->4
head = Node(4, Node(3, Node(4, Node(1, Node(4)))))
print(toString(removeDuplicateNodes(head)) == "3->1")
 
 # 6->8->3->4->4
head = Node(6, Node(8, Node(3, Node(4, Node(4))))) 
print(toString(removeDuplicateNodes(head)) == "6->8->3")
 
 # 6->6->8->3->4
head = Node(6, Node(6, Node(8, Node(3, Node(4))))) 
print(toString(removeDuplicateNodes(head)) == "8->3->4")
 
 # 6->6->8->4->4
head = Node(6, Node(6, Node(8, Node(4, Node(4))))) 
print(toString(removeDuplicateNodes(head)) == "8")
 
 # 6->6->5->5->5
head = Node(6, Node(6, Node(5, Node(5, Node(5))))) 
print(toString(removeDuplicateNodes(head)) == "<empty>")
 
 # 1->1->1->1->1
head = Node(1, Node(1, Node(1, Node(1, Node(1))))) 
print(toString(removeDuplicateNodes(head)) == "<empty>")
        