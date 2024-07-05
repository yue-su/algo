'''
Convert Binary Tree to Sorted Doubly Linked List

Given a Binary Tree(BT), convert it to a Doubly Linked List(DLL) in place. The left and right pointers in nodes are to be used as previous and next pointers, respectively, in the converted DLL. The order of nodes in DLL must be the same as the in -order traversal of the given Binary Tree. The first node of the in -order traversal(leftmost node in BT) must be the head node of the DLL.

As an example, the tree:
   2
  ↙ ↘
 1   3

starts out with the left and right pointers in the root node set, but the left and right pointers of both children are null since they are the leaf nodes. We're going to re-thread this by updating the pointers so that the nodes are now shaped like a doubly linked list:
null ← 1 ↔ 2 ↔ 3 → null

Now, only the left pointer of the 1 node is null, and the right pointer points to node 2. The right pointer of the 3 node is also still null, but its _left_ pointer points to node 2. The head of the list that should be returned is a pointer to the 1 node.

Note, that the examples here are all binary search trees because the in-order traversal will result in a sorted output list. This makes constructing and checking the code easy, but nothing in this solution should depend on the input being a BST.
 

EXAMPLE(S)
    3
  ↙  ↘
1      5
 ↘    ↙
  2  4

bt2dll(t) = "1 <-> 2 <-> 3 <-> 4 <-> 5"
 

FUNCTION SIGNATURE

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function bt2dll(root)

APPROACH

Traverse binary tree in order
------------------------------

- Recursively

1. Base case: if root is null, return null
2. If left exists, traverse down left child
3. If right exists, traverse down left child


Incorporate DLL into traversal
------------------------------

1. Base case: if root is null, return null
2. If left exists, traverse down left child
  a. recursively call function, passing in our previous pointer
3. If right exists, traverse down left child
  a. recurisvely call function, passing in our current root

*/

/* node for tree */

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

/* create a tree */

function treeFromArray(arr) {
    function insertLevelOrder(arr, i) {
        let root = null;
        // Base case for recursion
        if (i < arr.length) {
            root = new TreeNode(arr[i]);

            // insert left child
            root.left = insertLevelOrder(arr, 2 * i + 1);

            // insert right child
            root.right = insertLevelOrder(arr, 2 * i + 2);
        }
        return root;
    }

    return insertLevelOrder(arr, 0);
}

/* view a tree */

function printTree(root) {
    let m=findHeight(root);
    let n=Math.pow(2,m)-1;
    let result=[];

    for(let i=0; i<m; i++){
        result.push([]);
        for(let j=0; j<n; j++){
            result[result.length - 1].push('');
        }
    }

    function findHeight(root) {
        if (!root) return 0;

        return 1 + Math.max(findHeight(root.left), findHeight(root.right));

    }

    function fill(root,start=0,end=result[0].length-1,row=0){

        if(!root) return;

        let column=Math.floor((start+end)/2);

        result[row][column]=root.value.toString();

        if(root.left)
        fill(root.left,start,column-1,row+1);

        if(root.right)
        fill(root.right,column+1,end,row+1);

    }

    fill(root);

    return result;
};

/* node for linked list */

class ListNode {
    value;
    previous;
    next;

    constructor(value) {
      this.value = value;
      this.previous = null;
      this.next = null;
    }
  }

/* view a linked list */

function linkedListToArray(head) {
  let currentNode = head;
  let nodeValues = [];

  while (currentNode) {
    nodeValues.push(currentNode.value);
    currentNode = currentNode.next;
  }

  return nodeValues;
}

let root = treeFromArray([1, 2, 3, 4, 5, 6, 7])

console.table(printTree(root))

/* front-to-back */

function bt2dll(root, prev = null) {
  if (!root) return null;

  if (root.left)
    prev = bt2dll(root.left, prev)

  
  root.left = prev

  if (prev)
    root.right = root

  if (root.right)
    root = bt2dll(root.right, root)

  return root
}

/* back-to-front */

function bt2dll(root, listTail = null) {
  if (!root) return listTail;

  if (root.right) {
    listTail = bt2dll(root.right, listTail);
  }

  let listHead = root;
  listHead.right = listTail;
  if (listTail) {
    listTail.left = listHead;
  }

  if (root.left) {
    listHead = bt2dll(root.left, listHead);
  }

  return listHead;
}
'''


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def convert(root, prev):
            if root.left:
                prev = convert(root.left, prev)

            root.left = prev

            if prev:
                prev.right = root

            if root.right:
                root = convert(root.right, root)

            return root

        tail = convert(root, None)
        p = tail
        while p.left:
            p = p.left
        p.left = tail
        tail.right = p

        return p
