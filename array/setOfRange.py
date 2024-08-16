''' /*

develop a class called setOfRanges()
where you have: 
a function called insert that takes 2 numbers 
a function called query returns True or False depending on if the number exists in the range(s) 

input -> 2 integers, 2,2  1,1
output ->  [2,2]

i -> 1,5 
q -> 3 T
i -> 4,12
q -> 15 F  
*/

'''

class setOfRanges:
    def __init__(self):
        self.ranges = []

    def insert(self, num1, num2):
        if not self.ranges:
            self.ranges.append([num1, num2])
            return

        for range_ in self.ranges:
            start, end = range_
            if num1 <= end:
                new_start = min(start, num1)
                new_end = max(end, num2)
                range_[0] = new_start
                range_[1] = new_end
                return

        self.ranges.append([num1, num2])
        self.ranges.sort(key=lambda x: x[0])
        return

    def query(self, num):
        left = 0
        right = len(self.ranges) - 1

        while left <= right:
            mid = left + (right - left) // 2
            start = self.ranges[mid][0]
            end = self.ranges[mid][1]

            if start <= num and end >= num:
                return True
            elif start > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


ranges = setOfRanges()
ranges.insert(1.1, 4.4)
ranges.insert(5.1, 7.4)
ranges.insert(9.1, 10.4)
ranges.insert(9.05, 10.34)
print(ranges.query(0.9) == False)
print(ranges.query(1.6) == True)
print(ranges.query(3.6) == True)
print(ranges.query(4.6) == False)
print(ranges.query(5.6) == True)
print(ranges.query(7.6) == False)
print(ranges.query(9.6) == True)
print(ranges.query(10.99) == False)
