'''
❓ PROMPT
The infrastructure department of our city is evaluating the coverage and efficiency of the placement of street lamps. Ideally we want locations on the roads to be covered by one light.

Each light on a road has a position along that road (an integer) and a radius. A light at a point P with radius R lights the road at positions from `P - R` to `P + R`, inclusive.

Given an array of lamps, each being a 2 value array of `[position, radius]`, how many locations are lit by exactly one light?

Example(s)
litByOneLight([[1, 1],[2, 1]]) => 2
litByOneLight([[1, 1]]) => 3
litByOneLight([[1, 1], [2, 1]]) => 2
litByOneLight([[1, 1], [3, 1]]) => 4
litByOneLight([[1, 1], [4, 1]]) => 6

 

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
function litByOneLight(lamps)
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def litByOneLight(lamps):
    lamp_map = {}
    res = 0
    for lamp in lamps:
        location, radius = lamp
        for i in range(location - radius, location + radius + 1):
            if i in lamp_map:
                lamp_map[i] += 1
                res -= 1
            else:
                lamp_map[i] = 1
                res += 1

    return res


print(litByOneLight([[1, 1]]) == 3)
print(litByOneLight([[1, 1], [2, 1]]) == 2)
print(litByOneLight([[1, 1], [3, 1]]) == 4)
print(litByOneLight([[1, 1], [4, 1]]) == 6)
print(litByOneLight([]) == 0)
print(litByOneLight([[1, 0]]) == 1)
print(litByOneLight([[5, 2]]) == 5)
print(litByOneLight([[5, 2], [4, 1], [6, 1]]) == 0)
print(litByOneLight([[-5, 2], [-4, 1], [-6, 1]]) == 0)
print(litByOneLight([[-5, 2]]) == 5)