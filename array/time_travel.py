
'''
❓ PROMPT
Imagine you possess a time machine and have an array of years called 'years.' You begin your journey at year 'years[0]' and sequentially travel to years[1], years[2], and so on. Your objective is to determine the total time needed to visit each year in the list in the given order.

The time taken to travel from year A to year B is computed as follows:

0 hours if A = B
1 hour if A < B (traveling forward in time)
2 hours if A > B (traveling backward in time)

Example(s)
* For years = [1900, 1800, 1950, 2000], the output should be solution(years) = 4.
    * First, you travel from 1900 to 1800, which takes 2 hours.
    * Next, you travel from 1800 to 1950, which takes 1 hour.
    * Finally, you travel from 1950 to 2000, which takes 1 hour.
    * Overall, the journey requires 2 + 1 + 1 = 4 hours.

* For years = [1980, 2000, 1990], the output should be solution(years) = 3.
    * Initially, you travel from 1980 to 2000, which takes 1 hour.
    * Then, you travel from 2000 to 1990, which takes 2 hours.
    * In total, the journey requires 1 + 2 = 3 hours.

* For years = [2000, 2000, 1980], the output should be solution(years) = 2.
    * First, you travel from 2000 to 2000, which takes 0 hours as both years are the same.
    * Next, you travel from 2000 to 1980, which takes 2 hours.
    * Overall, the journey requires 0 + 2 = 2 hours.
 

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
function timeMachine(years) // returns an int of time travelled.
def time_machine(years: list) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def time_machine(years: list) -> int:
    if not years or len(years) == 1:
        return 0

    p = 1
    res = 0

    while p < len(years):
        curr = years[p]
        pre = years[p-1]
        if curr > pre:
            res += 1
        elif curr < pre:
            res += 2
        p = p+1

    return res


# Test Case 1: Array of length 1 (no travel)
years1 = [2000]
print(time_machine(years1) == 0)

# Test Case 2: Array of length 2 (going forward)
years2 = [2000, 2020]
print(time_machine(years2) == 1)

# Test Case 3: Array of length 2 (going backward)
years3 = [2020, 2000]
print(time_machine(years3) == 2)

# Test Case 4: Array of length 3 (going forward)
years4 = [2000, 2010, 2020]
print(time_machine(years4) == 2)

# Test Case 5: Array of length 3 (going forward and backward)
years5 = [2000, 2020, 2010]
print(time_machine(years5) == 3)

# Test Case 6: Array of length 5 (combination of going forward, backward, and staying in the same year)
years6 = [2000, 2010, 2010, 2005, 2020]
print(time_machine(years6) == 4)
