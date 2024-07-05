
'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums

    def reset(self) -> List[int]:
        return self.data

    def shuffle(self) -> List[int]:
        res = self.data.copy()
        index = len(res) - 1
        while index >= 0:
            random_number = randint(0, index)
            res[index], res[random_number] = res[random_number], res[index]
            index -= 1
        return res
