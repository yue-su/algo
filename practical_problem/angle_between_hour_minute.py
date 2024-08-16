
'''
❓ PROMPT
Given a time in the hh:mm format, return the angle (to the closest whole degree) between the hour and the minute hands.

As a follow-up, find all the times when the angle between both hands is 0.

Example(s)
calcluateAngle(12:00) returns 0
calcluateAngle(12:30) returns 165
calcluateAngle(12:31) returns 171
calcluateAngle(11:59) returns 6
 

🔎 EXPLORE
List your assumptions & discoveries:
minute position = minute
hour position = hour + minute * 10 / 60
delta = minute position - hour position

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function calculateAngle(time) {
def calculateAngle(time: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import math


def calculateAngle2(time: str) -> int:
    hour, minute = [int(x) for x in time.split(":")]
    delta = minute - (hour * 5 + minute * 5 / 60)
    degree = math.ceil(abs((delta / 60) * 360))
    return degree if degree < 180 else 360 - degree


def calculateAngle(time):
    timeComponents = list(map(int, time.split(':')))

    hour = timeComponents[0]
    minute = timeComponents[1]

    minuteAngle = 6 * minute
    hourAngle = 30 * hour + 0.5 * minute

    difference = abs(hourAngle - minuteAngle)

    return round(min(difference, 360 - difference))


def findAll():
    res = []
    for i in range(0, 12):
        for j in range(0, 60):
            time_string = f"{i}:{j}"
            if calculateAngle(time_string) <= 3:
                res.append(time_string)

    return res


print(findAll())


print(calculateAngle("12:00") == 0)
print(calculateAngle("12:30") == 165)
print(calculateAngle("12:31") == 171)
print(calculateAngle("11:59") == 6)
print(calculateAngle("1:42") == 159)
print(calculateAngle("3:30") == 75)
