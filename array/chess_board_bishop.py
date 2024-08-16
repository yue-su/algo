'''
Given a chess board with a set of bishops, return the number of pairs of bishops that are attacking each other. 
Bishops will be given as an array of tuples.
 

EXAMPLE(S)
Bishops: [(0, 0), (2, 2), (1, 2), (3, 0)]
This would look like this:

x . . . .
. . x . .
. . x . .
x . . . .
. . . . .

In this case, there are 2 pairs of bishops attacking each other.
Result = [(0,0), (2,2)], [(3,0),(1,2)] 
 

FUNCTION SIGNATURE
def numberOfBishops(bishops): Int
function pairsOfAttackingBishops(bishops)

'''


def numberOfBishops(bishops):
    pairs = 0
    additions = {}
    substractions = {}

    for row, col in bishops:
        addition = row + col
        substraction = row - col

        if addition not in additions:
            additions[addition] = 0
        else:
            additions[addition] += 1
            pairs += additions[addition]

        if substraction not in substractions:
            substractions[substraction] = 0
        else:
            substractions[substraction] += 1
            pairs += substractions[substraction]

    return pairs


print(numberOfBishops([[0, 0], [2, 2], [4, 4], [3, 0]]))
print(numberOfBishops([(0, 0), (2, 2), (1, 2), (3, 0)]))
