
'''
❓ PROMPT
You are given an array of numbers from 1 to N, except there is an extra! You have N + 1 numbers because one of them is in there twice! The array isn't sorted. Find the duplicated number without modifying the array.

Challenge: can you do this without using any extra space? 

Example(s)
[1, 2, 3, 2] -> 2
[6, 3, 4, 4, 2, 5, 1] -> 4
 

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
function findDuplicate(nums)
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findDuplicate(nums: list[int]) -> int:
    if not nums:
        return -1
    N = len(nums) - 1
    arith_sum = (N * (N + 1)) // 2
    total = sum(nums)

    return total - arith_sum