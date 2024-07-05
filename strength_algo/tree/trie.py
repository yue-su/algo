""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Implement a trie with insert, search, and startsWith methods.

Note:
• A trie is a tree-like data structure whose nodes store the letters of an alphabet.
• By structuring the nodes in a particular way, words and strings can be retrieved from the structure by traversing down a branch path of the tree.
• You may assume that all inputs are consist of lowercase letters a-z.
• All inputs are guaranteed to be non-empty strings.

Examples:
// trie = Trie()
// trie.insert("apple")
// trie.search("apple") // returns True
// trie.search("app") // returns False
// trie.startsWith("app") // returns True
// trie.insert("app")
// trie.search("app") // returns True

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
 """

from test_case import Test, TreeNode


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    # Write your code here.

    # Initialize your data structure here.
    def __init__(self):
        # Write your code here.
        self.head = Node()

    def _traverse(self, word):
        p = self.head
        for letter in word:
            if letter not in p.children:
                return None
            p = p.children[letter]
        return p

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        # Write your code here.
        p = self.head
        for letter in word:
            if letter not in p.children:
                p.children[letter] = Node()
            p = p.children[letter]
        p.is_end = True

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        # Write your code here.
        p = self._traverse(word)
        return p is not None and p.is_end

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        # Write your code here.
        return self._traverse(prefix) is not None


test = Test()
# Test Cases
test.startProblem("Trie")
trie = Trie()
trie.insert("apple")
test.test(True, trie.search("apple"), 1)
test.test(False, trie.search("app"), 2)
test.test(True, trie.startsWith("app"), 3)
trie.insert("app")
test.test(True, trie.search("app"), 4)
test.test(True, trie.startsWith("a"), 5)
test.test(False, trie.startsWith("ple"), 6)
test.endProblem()
