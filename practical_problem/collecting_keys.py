
'''
Today, you will be given the problem to collect keys.

You are moving out the office and need to collect everyone's keys before they leave. 
Unfortunately, everyone has different schedules so you can't just collect all the keys at once. 
You want to visit the office as few times as possible to collect everyone's keys.

Given a [[Int]] representing people's schedules, return the least number of times you'll need to visit to collect keys.
 

EXAMPLE(S)
[[10, 16], [2, 8], [1, 6], [7, 12]]

Should return 2. You could visit at 6 and then at 10 to collect all the keys.
 

FUNCTION SIGNATURE
func minVisits(schedule: [[Int]]) -> Int

1. use a start to track the start time at each schedule, end to track the end time
2. if the item in the schedules schedule[0] < end, there is a overlap, update the end with min(end, schedule[1])
3. if no overlap, append the current end to the res

'''


def minVisits(schedules):
    if not schedules:
        return 0

    schedules.sort(key=lambda x: x[0])

    _, end = schedules[0]

    res = []

    for i in range(1, len(schedules)):
        current_schedule = schedules[i]
        if current_schedule[0] <= end:
            end = min(end, current_schedule[1])
            # start = max(start, current_schedule[0])
        else:
            res.append(end)
            # start = current_schedule[0]
            end = current_schedule[1]

    res.append(end)
    print(res)

    return len(res)


s1 = [[10, 16], [2, 8], [1, 6], [7, 12]]  # 2
s2 = [[1, 6], [2, 8], [7, 12], [14, 16], [21, 25]]  # 4

print(minVisits(s1))
print(minVisits(s2))


def collect_keys(schedules):
    # sort the schedules in ascending order by the start time
    schedules.sort(key=lambda x: x[0])

    # initialize the number of visits to the office
    num_visits = 0

    # initialize the end time of the previous schedule
    prev_end = 0

    # for each schedule
    for schedule in schedules:
        # if the start time of the schedule is before the end time of the previous schedule, then we don't need to visit the office again
        if schedule[0] <= prev_end:
            continue

        # otherwise, we need to visit the office again
        num_visits += 1

        # update the end time of the previous schedule
        prev_end = schedule[1]

    # return the total number of visits to the office
    return num_visits
