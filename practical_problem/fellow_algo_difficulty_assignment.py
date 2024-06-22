'''
Formation is trying to assign a group of Fellows algorithms of varying difficulty levels. The algorithm difficulty should feel fair to all Fellows based on each Fellow's algorithmic skill level.

We are given an array of integers representing the skill level of each Fellow, and we are asked to return an array of integers representing the difficulty of an algorithm to assign each Fellow respectively.

The minimum difficulty is 1. When a Fellow has a higher skill level than an adjacent Fellow they must be given a more difficult problem than their neighbor. When a fellow has the same skill level, they must be given a problem at the same difficulty level. Return the array of difficulties representing the minimum difficulty we can give each Fellow.
 

EXAMPLE(S)
fellows = [10, 20, 60, 70, 50, 10, 20]
          [1, 2, 3, 4, 1, 1, 2]
          [1, 2, 3, 4, 2, 1, 2]
assignAlgorithms(fellows) -> [1,2,3,4,2,1,2]

Text of Algorithm:

0. set a res = []
   set the res[0] to 1
1. loop from 1 to len(fellows) - 1
      if current fellow skill < prev fellow skill:
        set the res[current] = res[current - 1]++
      else if current == pre
        move to the prev and set the value to the pre 

2. loop from the last to 0
      check if the pre > current:
        set the pre difficulty to pre++

FUNCTION SIGNATURE
def assignAlgorithms(fellows: list[int]) -> list[int]:
'''


def assignAlgorithms(fellows: list[int]) -> list[int]:
  res = [1] * len(fellows)

  r = 1

  while r < len(fellows):  # [10, 20, 60, 70, 50, 10, 20]
    prev = res[r-1]
    if fellows[r] > fellows[r-1]:
      res[r] = prev+1
    elif fellows[r] == fellows[r-1]:
      res[r] = res[r-1]

    r += 1
  print(res)

  last = len(fellows) - 2

  while last > 0:

    if fellows[last] > fellows[last + 1]:
      if res[last] > res[last + 1]:
        pass
      else:
        res[last] += 1

    last -= 1

  return res


print(assignAlgorithms([10, 20, 60, 70, 50, 10, 20]))  # [1,2,3,4,2,1,2]
