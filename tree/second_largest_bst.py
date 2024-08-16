
'''
Find the second largest element in a BST.
 

EXAMPLE(S)
  2
 / \
1   3

In this tree, return 2.
 

FUNCTION SIGNATURE
func secondLargest(node: Node) -> Int

successor
predecessor
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree_1 = Node(8, left=Node(5, left=Node(2, left=Node(1)), right=Node(
    6, right=Node(7))), right=Node(10, left=Node(9), right=Node(11, right=Node(12))))
tree_2 = Node(8, left=Node(5, left=Node(2, left=Node(1)), right=Node(
    6, right=Node(7))))
tree_3 = None
tree_4 = Node(1)

'''
        8
    5       10
  2   6   9    11
1      7          12   
'''

def predecessor(root):
    pass

def successor(root):
    pass


def secondLargest_1(node: Node):

    count = 0
    res = 0

    def dfs(root):
        nonlocal count, res
        if not root:
            return

        dfs(root.right)
        count += 1
        if count == 2:
            res = root.value
        dfs(root.left)

    dfs(node)
    return res


def secondLargest(root):
    # root == None
    if not root:
        return -1
    # if there is a right
    if root.right:
        result = secondLargest(root.right)
        return result if result != -1 else root.value
    # no right but left
    if root.left:
        curr = root.left
        while curr.right:
            curr = curr.right
        return curr.value

    # not right and not left
    return -1


print(secondLargest(tree_1))
print(secondLargest(tree_2))
print(secondLargest(tree_3))
print(secondLargest(tree_4))
