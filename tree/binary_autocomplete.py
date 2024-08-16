'''
The programming interface for a legacy motor controller accepts commands as binary strings of variable length. The console has a very primitive autocomplete autocorrect feature: given an incomplete command, it will display possible commands that has the incomplete command as a prefix. For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result. 

Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.
 

EXAMPLE(S)
Possible commands = ['000', '1110', '01', '001', '110', '11',]

'0' → ['000', '01', '001'] 
'1' → ['1110', '110', '11']
'00' → ['000', '001']
'1110' →['1110']

edge cases:
'010101010' -> [] 
'' -> [...]
Order of the return output --> can be in any order
no duplicate commands


Approaches:


Possible commands = ['000', '1110', '01', '001', '110', '11',]
q = query

O(q * n)


1. Brute force         *
     ['000', '1110', '01', '001', '110', '11',]
  01
    this.data = commands
    - Traverse through array, check each command to see if a match


2. Trie / Prefix 
- store commands in the tree, each command represents a path in the tree

Possible commands = ['000', '1110', '01', '001', '110', '11',]


Trie.add(command)
Trie.add("000") O(n * c)

O(c)


Possible commands = ['000']

0 -> '000'

O(m + n)
m = length of prefix 
n = number of characters in all matched strings -> total size of strings -> t

Node
  val, left, right


class TrieNode {
  constructor(val) {
    this.val = val;
   0 this.left = 
   1 this.right = 
    this.isEnd = false;  *
  }
}

    01 --> ['000', '01', '001'] 

    01
              root    
           0        1
        0     1(here       1
      0*   1*   





FUNCTION SIGNATURE
Implement a class that should be initialized with a list of possible commands. The class should have the following public method:

autocomplete(command) {
def autocomplete(self, command: str) -> list[str]:


[Link](https://www.youtube.com/watch?v=1Vhide0vVqU)
[Auto complete trie in Javascript](https://github.com/ashtable/autocomplete-trie-in-javascript)
'''
