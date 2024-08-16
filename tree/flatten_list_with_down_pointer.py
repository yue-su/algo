'''
For this problem, the normal linked list is modified linked list with a "down" pointer in addition to the normal value and next pointer. "Flatten" this linked list into a single linear thread using only the next pointers. From any given node, anything in it's "down" list comes before the "next" list.
 

EXAMPLE(S)
1 -> 6  
 2
  5  

In this example:
1.next == 6, 1.down == 2, 2.down == 5

Output:
1 -> 2 -> 5 -> 6

Always resolve down before next.
 

FUNCTION SIGNATURE
class LLNode {
  constructor(value, next = null, down = null) {
    this.value = value;
    this.next = next;
    this.down = down;
  }
}

func flatten(node: Node)
'''

def flatten(node):
    