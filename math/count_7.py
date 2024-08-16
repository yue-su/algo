
'''
❓ PROMPT
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. 
Use recursion to solve this problem (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while integer division by 10 removes the rightmost digit (126 / 10 is 12). 
Be aware that some languages require some special handling to do integer division while others do not.

*Python integer division*: x // y
*Javascript integer division*: Math.floor(x / y)

Example(s)
count7(7) == 1
count7(123) == 0
count7(717) == 2
 

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
function count7(n) {
def count7(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def count7(n: int) -> int:

    def helper(n):
        if n == 0:
            return 0

        if n % 10 == 7:
            return 1 + helper(n // 10)

        else:
            return helper(n // 10)

    return helper(n)


print(count7(717) == 2)
print(count7(7) == 1)
print(count7(5) == 0)
print(count7(123) == 0)
print(count7(77) == 2)
print(count7(7123) == 1)
print(count7(771237) == 3)
print(count7(771737) == 4)
print(count7(47571) == 2)
print(count7(777777) == 6)
print(count7(70701277) == 4)
print(count7(777576197) == 5)
print(count7(99999) == 0)
print(count7(99799) == 1)
