
'''
True Summits

While on a hike, you are standing on the trail, looking up a peak, and wondering if it is the top of the mountain: the true summit. But the highest point is not always in view. It may be obscured by a false summit, a position that is lower than the true summit but stands in the way and obscures the highest point from view. For example:

                              /
            / \             /
          /     \ _ _ _ _ /
        /
    _ /
X /
0 1 1 2 3 4 5 4 3 3 3 3 3 4 5 6 - elevations

In this case, the person standing at the X is looking up at a peak 6 units away that is 5 units high. So even though there is a higher peak further back, it can't be seen because a false summit is in the line of site. So for input [0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 3, 3, 3, 4, 5, 6], the result should be false; you cannot see the true summit, because there is another point in the way, blocking the view.

                    | \
                    |   \
                    |     \
                    |       _ _
                    |
                    |
                    |
            / \     |
          /     \ _ |
        /
    _ /
X /

0 1 1 2 3 4 5 4 3 3 11 10 9 8 7 7 - elevations

                    
                    | \    
                    |  \ 
                    |    _ _
                    |
                    |
            / \     |
          /     \ _ |
        /
    _ /
X /

0 1 1 2 3 4 5 4 3 3 9 8 7 7 - elevations

maxht = 5
point = 5
slope = 9/10 = 0.9

maxVisible = 
APPROACH: 
  - maxHt = 0
  - maxSlope = 0
  - maxSlopeVisible = True (by default)


The input [0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 11, 10, 9, 8, 7, 7] will return true because the true summit is tall enough to be seen above everything in the foreground. However, if the value 11 is instead a 9, the true summit will be obscured by the value 1 at the second index. The value 1 then becomes a false summit!

We can think about this from an urban perspective also! Imagine you are standing on a sidewalk somewhere in Manhattan. As you look around you, can you see the top of the tallest building on the island, One World Trade Center? From some positions, it is visible, but from most, it is not. Shorter buildings are standing in the way: Consider this situation where one building obscures a taller one behind it:

                  |
                  |
             |    |
             |    |
             |    |
             |    |
             |    |
             |    |
             |    |
          X  |    |
  Height: 0  8  0  10
Position: 0  1  2  3  4  5  6

The function takes an array of elevations. The first elevation (at index 0) will be zero and is the position of the viewer. From there, the elevations at each position will potentially change and indicate the elevation at that point relative to the viewpoint. Return true if the highest visible point is the true summit.

* For a visualization of the 3 examples, please view the Verbal Explaination spoiler section
 

EXAMPLE(S)
canSeeTrueSummit([0, 1, 2, 3, 4, 5]) == true
canSeeTrueSummit([0, 2, 3]) == false
canSeeTrueSummit([0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 9, 9, 9, 8, 7, 7]) == false
canSeeTrueSummit([0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 11, 10, 9, 8, 7, 7]) == true
 

FUNCTION SIGNATURE
function canSeeTrueSummit(elevations)

Questions/Revealing TestCase: 
  1. Are we always going to start from 0?
  2. we will have atleast 2 entries eg [0,2,3] or [0,-1]
  3. max peak is always 1
  4. we can calculate slope based on x and y axis where x axis = index, y = elevation[index]
  5. our starting point can be the highest point eg [0, -1]

Explore: 

  1. find the max peak and index in the frist iteration

[0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 9, 9, 9, 8, 7, 7]

max_value = 9
max_index = 10

slope_max = max_value / max_index = 9/10 = 0.9

  2. iterate from 0 to 9

sec_max_value = 5
sec_max_index = 6

slope_before_max = 5 / 6 = 0.7

  3. if slope_max > slope_before_max:
          return True

maxSlopeVisible = True (Take cake of test case #5)

Approach 1 (Cleaner):
 - for loop on elevations:
   - calculate the slope for each elevation
    - curr_slope = elevation[index]/index
   - if this point > maxHeight
      - maxHeight = point
      - if this curr_slope >= maxSlope
          - maxSlopeVisible = True
        else:
           maxSlopeVisible = False

    maxSlope = max(slope, maxSlope)
- return maxSlopeVisible


Runtime: O(n), where n is length of elevation 
Space: O(1) 
'''


def maxPeakVisible(elevations):
  maxHeight = 0
  maxSlope = 0
  maxSlopeVisible = True
  for i in range(1, len(elevations)):
    point = elevations[i]
    curr_slope = point/i
    if point > maxHeight:
      maxHeight = point
      if curr_slope >= maxSlope:
        maxSlopeVisible = True
      else:
        maxSlopeVisible = False
    maxSlope = max(maxSlope, curr_slope)
  return maxSlopeVisible


print(maxPeakVisible([0, 1, 2, 3, 4, 5]) == True)
print(maxPeakVisible([0, 2, 3]) == False)
print(maxPeakVisible([0, -1]) == True)
print(maxPeakVisible(
    [0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 11, 10, 9, 8, 7, 7]) == True)
print(maxPeakVisible([0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 9, 9, 8, 7, 7]) == False)
