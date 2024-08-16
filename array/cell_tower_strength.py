'''

You are given an array representing the positions of cell towers along a 1-dimensional line. 
You are given a second array representing customers' positions along the same line. 
Given these two inputs, you must determine the minimum signal strength *k* such that every customer is covered by at least one cell tower. 
All cell towers must have the exact same signal strength and cover customers to their left and right equally.

These arrays can be imagined as street addresses along a road. At each address, there might be a customer, and there might also be a tower at that location.
 
EXAMPLE(S)
Let's say cell towers are at: [0, 2, 6, 10]
and customers are at: [0, 5, 11]

In this case, you only need a cell distance of 1, because customer 5 would be covered by 6 and customer 11 would be covered by 10.

If the customers were at: [0, 4, 13], you'd need a distance of 3 in order for customer 13 to be covered by 10.
 

FUNCTION SIGNATURE
def search(customers: list[int], towers: list[int]) -> int:

'''


def search(customers, towers):

    t = 0
    min_range = float('-inf')

    for customer in customers:

        while t < len(towers) - 1 and towers[t] <= customer:
            t += 1
            if towers[t] > customer:
                range = min(towers[t] - customer, customer - towers[t - 1])
            else:
                range = customer - towers[t]

            min_range = max(min_range, range)
    print("tower stop at:", t)

    return min_range if min_range != float('-inf') else 0


towers = [0, 2, 6, 10]
customers = [0, 5, 11]
print(search(customers, towers))

towers = [0, 2, 6, 10]
customers = [0, 4, 13]
print(search(customers, towers))


towers = [3]
customers = [3]
print(search(customers, towers))

towers = [2, 6]
customers = [4]
print(search(customers, towers))

'''
Towers: [0, 2, 6, 10]
Customers:[0, 5, 11]
Result: 1

Towers: [3]
Customers: [3]
Result: 0

Towers: [2, 6]
Customers: [4]
Result: 2
'''
