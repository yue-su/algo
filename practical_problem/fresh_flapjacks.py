
'''
❓ PROMPT
You're the manager of a flapjack (pancake) shop. At the end of the day, you get a printed record of every batch of flapjacks added to the serving area and every batch that's removed because an order comes in.

The record looks like a series of positive and negative integers, so that, e.g., [2, -1, 3, -2, -1] means

2 pancakes are ready and put on the serving area
1 pancake went out for an order
3 pancakes are done cooking and ready
2 pancakes went out for an order
1 pancacke went out for an order

As the manager, you want orders to go out immediately but also don't want too many pancakes piling up in the serving area. You want to make sure that there are never more than 4 pancakes in the stack, waiting to be served, but also that orders of two or less are always served immediately. The stack can be empty, so long as it is refreshed before the next order comes in.

Part 1)
  Write a function that takes an end-of-day record and that returns true or false to indicate whether the constraints were satisfied.

Part 2)
  If the cooks got ahead, you also want to know how far ahead. Modify the function to return a pair. The first item in the pair is the same as in part 1, just true or false indicating whether the constraints were satisfied or not. The second value in the pair should be the maximum height of the stack during the day.

Example(s)
freshFlapjacks([2, -1]) => [true, 2]
freshFlapjacks([-1, 2]) => [false, 1]
freshFlapjacks([2, -1, 3, -3, 2, -1]) => [true, 4]
 

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
function freshFlapjacks(pancakes) {
def freshFlapjacks(pancakes: list[int]) -> list:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def freshFlapjacks(pancakes: list[int]) -> list:
    initial = 0
    max_height = 0
    res = True

    for pancake in pancakes:
        initial += pancake
        if initial < 0 or initial > 4:
            res = False
        max_height = max(initial, max_height)

    return [res, max_height]


print(freshFlapjacks([2]) == [True, 2])
print(freshFlapjacks([-2]) == [False, 0])
print(freshFlapjacks([4]) == [True, 4])
print(freshFlapjacks([5]) == [False, 5])
print(freshFlapjacks([4, -2, 1, -2]) == [True, 4])
print(freshFlapjacks([2, -1, 1, -1, 1]) == [True, 2])
print(freshFlapjacks([4, -2, 1, -2, 4]) == [False, 5])
print(freshFlapjacks([4, -2, 1, -2, -4]) == [False, 4])
