def find_available_slots(schedules: dict, duration: int) -> list:

  # merge all schedules
  merged_slots = []
  for value in schedules.values():
    merged_slots += value
  
  merged_slots.sort(key = lambda x:x[0])
  
  # early return if there is no slots in the merged_slots, which means all the slots are free
  if not merged_slots:
    return list(range(8,17))

  start = merged_slots[0][0]
  end = merged_slots[0][1]

  non_overlap_slots = []

  for schedule in merged_slots[1:]:
    curr_start, curr_end = schedule
    if curr_start <= end:
      end = max(curr_end, end)
    else:
      non_overlap_slots.append((start, end))
      start = curr_start
      end = curr_end
  # append the last one
  non_overlap_slots.append((start, end))

  # calculate free slots
  free_slots = []

  pre_end = 8

  for schedule in non_overlap_slots:
      curr_start, curr_end = schedule
      if curr_start - pre_end >= duration:
        free_slots.append((pre_end, curr_start))
      pre_end = curr_end
  
  # check if there are time left after the last slot till 17
  if 17 - pre_end >= duration:
    free_slots.append((pre_end, 17))

  available_slots = []

  # spread the slots over time
  for slot in free_slots:
    start_times = list(range(slot[0], slot[1] - duration + 1))
    available_slots += start_times

  return available_slots





find_available_slots({
        'Alice': [(8, 10), (13, 14)],
        'Bob': [(9, 11), (14, 15)],
        'Charlie': [(10, 12), (15, 16)],
    }
    ,2)

def test_find_available_slots():
    # Test case 1: No free slots available
    schedules = {
        'Alice': [(8, 10), (13, 14)],
        'Bob': [(9, 11), (14, 15)],
        'Charlie': [(10, 12), (15, 16)],
    }
    duration = 2
    assert find_available_slots(schedules, duration) == []

    # Test case 2: One free slot available
    schedules = {
        'Alice': [(8, 10), (13, 14)],
        'Bob': [(10, 11), (14, 15), (16, 17)],
        'Charlie': [(11, 12), (15, 16)],
    }
    duration = 1
    assert find_available_slots(schedules, duration) == [12]

    # Test case 3: Multiple free slots available
    schedules = {
        'Alice': [(8, 9), (10, 11), (13, 14)],
        'Bob': [(9, 10), (14, 15)],
        'Charlie': [(11, 12), (15, 16)],
    }
    duration = 1
    assert find_available_slots(schedules, duration) == [12, 16]

    # Test case 4: Free slots at start and end of workday
    schedules = {
        'Alice': [(9, 10), (11, 12), (13, 14)],
        'Bob': [(10, 11), (12, 13), (14, 15)],
        'Charlie': [(15, 16)],
    }
    duration = 1
    assert find_available_slots(schedules, duration) == [8, 16]

    # Test case 5: Two hour meeting
    schedules = {
        'Alice': [(10, 12), (15, 16)],
        'Bob': [],
        'Charlie': [(15, 16)],
    }
    duration = 2
    assert find_available_slots(schedules, duration) == [8, 12, 13]

    # Test case 6: All day free
    schedules = {
        'Alice': [],
        'Bob': [],
        'Charlie': [],
    }
    duration = 1
    assert find_available_slots(schedules, duration) == [8, 9, 10, 11, 12, 13, 14, 15, 16]

    # Test case 7: Multiple start times in block
    schedules = {
        'Alice': [(8, 11)],
        'Bob': [(11, 14)],
        'Charlie': [],
    }
    duration = 1
    assert find_available_slots(schedules, duration) == [14, 15, 16]

    # Test case 8: Meeting longer than workday
    schedules = {
        'Alice': [(8, 11)],
        'Bob': [(11, 14)],
        'Charlie': [],
    }
    duration = 10
    assert find_available_slots(schedules, duration) == []

    print("All tests passed!")

test_find_available_slots()