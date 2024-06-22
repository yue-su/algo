
'''
Question : 

You are given a series of inputs representing delivery events. Each event is represented by an array of length 3:

[1, 1591846068, 0]

- The first number is an order number
- The second number is the timestamp
- The third number is either 0 (representing a pickup) or 1 (representing a dropoff)

Given a series of events, return the total active time, calculated by the period of time where they have an active delivery (if they've dropped everything off, they are not considered active until they pick something up again).

**Follow-up**
Now, let's say the input is not guaranteed to be valid. What are some ways that the input could be invalid?

- Timestamps are not increasing
- A pickup is dropped off an incorrect number of times (0 or 2+ times)
- A dropoff occurs before a pickup, or the pickup does not exist

For any pickups and dropoffs that are invalid, ignore them entirely. Add one restriction at a time and have their code test for that condition.
 

EXAMPLE(S)
Input:
[1, 1591846068, 0] -
[2, 1591846070, 0]
[1, 1591846071, 1]
[2, 1591846080, 1] - 12
[3, 1591846090, 0]
[3, 1591846102, 1] - 12
                     24
Output: 24
 
[1, 1591846068, 0] 
[1, 1591846068, 1] => 0 active time 


Edge cases/Assumptions/Observations : 
- assume timestamp to be a number 
- timestamp in increasing order ****
- dropoffs/pickups are going to be in valid order ****
- every pickup has a dropoff ****
- 3rd entry might be irrelevant because first instance of an order is a pickup, second is a drop off

- 1st entry vs 3rd entry, which one do we consider irrelevant ? Both can be considered irrelevant, but not at the same time 



Approach : 
Approach #1 : 
3rd entry irrelevant : 
- variable to record total active time
- set inital timestamp 
- set to see what we picked up already
  - if dropoff, remove from set
- when our set is empty : take differnce between current timestamp and start time stamp and add to total active time

{}
start = 1591846090
total_active = (1591846080 - 1591846068) + (1591846102 - 1591846090)

[1, 1591846068, 0] 
[2, 1591846070, 0] 
[1, 1591846071, 1] 
[2, 1591846080, 1] - 12 
[3, 1591846090, 0] 
[3, 1591846102, 1] - 12 |

Analysis : 
Time complexity : O(N) 
Space complexity : O(N) because we are using a set 


Approach #2 : 
1st entry irrelevant : 
- similar solution, we keep a counter instead 

packages = 0
start = 1591846068
total_active = (1591846080 - 1591846068) + (1591846102 - 1591846090)

[1, 1591846068, 0] 
[2, 1591846070, 0] 
[1, 1591846071, 1] 
[2, 1591846080, 1] - 12 
[3, 1591846090, 0] 
[3, 1591846102, 1] - 12 |


Analysis : 
Time complexity : O(N) 
Space complexity : O(1)


FUNCTION SIGNATURE
function activeDeliveryTime(events) {
def activeDeliveryTime(events: [int]) -> int:
'''


'''
Follow up:
https://leetcode.com/problems/stone-game/description/
'''


def activeDeliveryTime(events: [int]) -> int:
    pass


print(activeDeliveryTime([
    [1, 1591846068, 0],
    [2, 1591846070, 0],
    [1, 1591846071, 1],
    [2, 1591846080, 1],
    [3, 1591846090, 0],
    [3, 1591846102, 1]]
)
)


print(activeDeliveryTime([]) == 0)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [1, 1591846072, 1]
    ]) == 4)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [1, 1591846072, 1],
        [2, 1591846073, 0],
        [2, 1591846078, 1]
    ]) == 9)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [2, 1591846070, 0],
        [1, 1591846072, 1],
        [2, 1591846078, 1]
    ]) == 10)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [2, 1591846070, 0],
        [1, 1591846071, 1],
        [2, 1591846080, 1],
        [3, 1591846090, 0],
        [3, 1591846102, 1],
    ]) == 24)
print(activeDeliveryTime([[1, 1591846068, 0]]) == 0)
print(activeDeliveryTime([[1, 1591846072, 1]]) == 0)
