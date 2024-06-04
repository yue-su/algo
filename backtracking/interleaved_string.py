
'''
❓ PROMPT
Given two strings *x* and *y* we can create an interleaving by repeatedly taking the first character of either and appending the characters together to form a new string. Specifically, valid interleavings will have these properties:

1. len(interleaving) == len(x) + len(y)
2. *interleaving - x = y* and *interleaving - y = x* meaning that removing the characters in *x* from the interleaving will produce *y* and vice versa.
3. x and y both appear as subsequences in the interleaving. The order of characters in x and y are preserved in the interleaving.

Given *x*, *y*, and *s*, write a function that determines whether *s* is a valid interleaving of *x* and *y*.

For this exercise, solve this with backtracking. There are [solutions](https://leetcode.com/problems/interleaving-string/solution/) with more efficient complexities that employ dynamic programming or recursion with memorization but they aren't expected for this task. We'll get to those later.

Example(s)
These are some valid interleaving using the strings *ABC* and *BCD*:

isInterleaving("ABC", "BCD", "BABCCD") == True
Explanation:
 x:             AB C
 y:            B  C D
 interleaving: BABCCD

isInterleaving("ABC", "BCD", "ABCBCD") == True
Explanation:
 x:            ABC
 y:               BCD
 interleaving: ABCBCD

isInterleaving("ABC", "BCD", "BCDABC") == True
Explanation:
 x:               ABC
 y:            BCD
 interleaving: BCDABC

isInterleaving("ABC", "BCD", "BCABDC") == True
Explanation:
 x:              AB C
 y:            BC  D
 interleaving: BCABDC

isInterleaving("ABC", "BCD", "BABCDD") == False
Explanation:
BABCDD cannot be created from the any combination of the sequences ABC & BCD
 

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
function isInterleaving(x, y, s) {
def is_interleaving(x: str, y: str, s: str) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def is_interleaving(x: str, y: str, s: str) -> bool:
    if len(s) != len(x) + len(y):
        return False
    
    track = []
    found = False

    def helper(i, j):
        nonlocal found

        if i==len(x) and j==len(y):
            if "".join(track) == s:
                found = True
            return
        
        if found:
            return
        
        if i < len(x):
            track.append(x[i])
            helper(i + 1, j)
            track.pop()
  
        
        if j < len(y):
            track.append(y[j])
            helper(i, j+1)
            track.pop()

    helper(0,0)

    return found





            
print(is_interleaving("XXXXX", "YYYYY", "shorter") == False)
print(is_interleaving("X", "Y", "longer") == False)
print(is_interleaving("X", "Y", "XY") == True)
print(is_interleaving("X", "Y", "YX") == True)
print(is_interleaving("X", "Y", "XX") == False)
print(is_interleaving("X", "Y", "YY") == False)
print(is_interleaving("ABC", "D", "ABCD") == True)
print(is_interleaving("ABC", "D", "ABDC") == True)
print(is_interleaving("ABC", "D", "ADBC") == True)
print(is_interleaving("ABC", "D", "DABC") == True)
print(is_interleaving("AABCC", "DBBCA", "AADBBCBCAC") == True)
print(is_interleaving("ABC", "BCD", "BABCCD") == True)
print(is_interleaving("ABC", "BCD", "ABCBCD") == True)
print(is_interleaving("ABC", "BCD", "BCDABC") == True)
print(is_interleaving("ABC", "BCD", "BCABDC") == True)
print(is_interleaving("ABC", "BCD", "BABCDD") == False)
print(is_interleaving("ABC", "BCD", "ABBCCD") == True)
print(is_interleaving("ABC", "BCD", "DCCBBA") == False)
print(is_interleaving("ABC", "BCD", "ABBDCC") == False)
print(is_interleaving("ABC", "BCD", "ACBBCD") == False)