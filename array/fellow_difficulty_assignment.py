'''
Formation is trying to assign a group of Fellows algorithms of varying difficulty levels. The algorithm difficulty should feel fair to all Fellows based on each Fellow's algorithmic skill level.

We are given an array of integers representing the skill level of each Fellow, and we are asked to return an array of integers representing the difficulty of an algorithm to assign each Fellow respectively.

The minimum difficulty is 1. When a Fellow has a higher skill level than an adjacent Fellow they must be given a more difficult problem than their neighbor. When a fellow has the same skill level, they must be given a problem at the same difficulty level. Return the array of difficulties representing the minimum difficulty we can give each Fellow.
 

EXAMPLE(S)
fellows = [10, 20, 60, 70, 50, 10, 20] -> 
assignAlgorithms(fellows) -> [1,2,3,4,2,1,2]

[20,20,10] -> [2,2,1]

[10,20,30,20]-> [1,2,3,1]


FUNCTION SIGNATURE
def assignAlgorithms(fellows: list[int]) -> list[int]:


Clarifications:
- Adjacent fellows with same skill , should have same algorithm difficulty
- Fellows with same skill need not have same difficulty algo


Brainstorm:
Approach 1:
    -> iterate start to end 
        give the first item a difficult of 1 and check if the next skill level is larger than the current one
            if prev is smaller, increment
            if prev is equal, assign the same with the previous one
            if prev is greater, reset the level to 1 and start from there
        
        [10, 20, 60, 70, 50, 10, 20]
    -> [1,  2,  3,  4,  1,  1,  2]

    -> [70, 50, 10, 20]
       [1,   1,  1,  2]

    -> [20, 20, 10]
       [1,   1,  1]
        
    - iterate end to start
        if current is larger than previous, increment the current difficult level by 1
               [10, 20, 60, 70, 50, 10, 20]
    -> lToR -> [1,  2,  3,   4,  2  1,  2]


         -> [70, 50, 10, 20]
            [1,   1,  1,  2]
            [3,  2,  1,   1]

        Max:   [3, 2,   1,   2]
    

Approach 2:

'''


def assignAlgorithms(fellows: list[int]) -> list[int]:
    res = [1]*len(fellows)
    for i in range(1, len(fellows)):
        if fellows[i] > fellows[i - 1]:
            res[i] = res[i-1] + 1
        elif fellows[i] == fellows[i - 1]:
            res[i] = res[i - 1]
        else:
            res[i] = 1

    for i in range(len(fellows) - 2, -1, -1):
        if fellows[i] > fellows[i + 1]:
            res[i] = max(res[i], res[i+1] + 1)
        elif fellows[i] == fellows[i + 1]:
            res[i] = max(res[i], res[i + 1])
        else:
            res[i] = max(res[i], 1)

    return res


print(assignAlgorithms([10, 20, 60, 70, 50, 10, 20]) == [1, 2, 3, 4, 2, 1, 2])
print(assignAlgorithms([70, 50, 10, 20]) == [3, 2, 1, 2])
print(assignAlgorithms([20, 20, 10]) == [2, 2, 1])


print(assignAlgorithms([10, 20, 60, 70, 50, 10, 20]) == [1, 2, 3, 4, 2, 1, 2])
print(assignAlgorithms([]) == None or assignAlgorithms([]) == [])
print(assignAlgorithms([100]) == [1])
print(assignAlgorithms([11, 22]) == [1, 2])
print(assignAlgorithms([22, 11]) == [2, 1])
print(assignAlgorithms([20, 20]) == [1, 1])
print(assignAlgorithms([20, 20, 5]) == [2, 2, 1])
print(assignAlgorithms([5, 20, 20]) == [1, 2, 2])
print(assignAlgorithms([19, 29, 39]) == [1, 2, 3])
print(assignAlgorithms([37, 27, 17]) == [3, 2, 1])
print(assignAlgorithms([10, 20, 100, 70, 100, 10, 20])
      == [1, 2, 3, 1, 2, 1, 2])
print(assignAlgorithms([32, 22, 12, 22, 32]) == [3, 2, 1, 2, 3])
print(assignAlgorithms([15, 25, 35, 25, 15]) == [1, 2, 3, 2, 1])
print(assignAlgorithms([15, 10,25,25,25,10,15]) == [2,1,2,2,2,1,2])