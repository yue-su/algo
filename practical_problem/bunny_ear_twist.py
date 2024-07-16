
'''
❓ PROMPT
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the usual 2 ears. 
The even bunnies (2, 4, ..) we'll say have 3 ears because they each have a raised foot. 
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

Example(s)
bunnyEarsTwist(2) == 5
bunnyEarsTwist(3) == 7
bunnyEarsTwist(5) == 12
 

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
function bunnyEarsTwist(bunnies) {
def bunnyEarsTwist(bunnies: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def bunnyEarsTwist(bunnies: int) -> int:
    if bunnies == 0:
        return 0

    if bunnies % 2 == 0:
        return 3 + bunnyEarsTwist(bunnies - 1)

    return 2 + bunnyEarsTwist(bunnies - 1)


print(bunnyEarsTwist(12) == 30)
print(bunnyEarsTwist(10) == 25)
print(bunnyEarsTwist(5) == 12)
print(bunnyEarsTwist(3) == 7)
print(bunnyEarsTwist(2) == 5)
print(bunnyEarsTwist(1) == 2)
print(bunnyEarsTwist(0) == 0)
