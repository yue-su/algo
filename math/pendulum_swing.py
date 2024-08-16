
'''
Given a distance d, a pendulum starts at d and swings from d to negative d and back. For example, given distance 3, the pendulum goes 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, and back again. 
Given a time t, return the pendulum's position. The time starts at 0.

In this example, 0 returns 3, 1 returns 2, 3 returns 0, and so on.
 

EXAMPLE(S)
Input: d = 5, t = 7
Output: -2
Explanation: The pendulum swings as follows, with the 7th tick on the -2 position.
5 4 3 2 1 0 -1 -2 -3 -4 -5
0 1 2 3 4 5  6   7
 

FUNCTION SIGNATURE
function pendulum(distance, time)

1. start from d
2. decrement d t*2 + 1 times -> incurement d t*2 + 1 times
3. a counter to track how many times, when counter == t, stop
4. a boolean to control the direction of inc/dec

'''


def pendulum(d, t):

  inc = False
  times = 0
  max_times = d*2

  while t > 0:
    if not inc:
      if times < max_times:
        d -= 1
      else:
        inc = True
        times = 0
        d += 1
    else:
      if times < max_times:
        d += 1
      else:
        inc = False
        times = 0
        d -= 1

    t -= 1
    times += 1

  return d
# when t = 10,
# t = 1 10 < max_times


'''
Follow-up:
What if the pendulum reduces by 1 distance per full swing? 
For example, for distance 3, the pendulum would go 
3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 0, -1, 0 
and then stay on 0 from this point forward.
'''

print(pendulum(3, 0))
print(pendulum(3, 1))
print(pendulum(3, 2))
print(pendulum(3, 3))
print(pendulum(3, 4))
print(pendulum(3, 5))
print(pendulum(3, 6))
print(pendulum(3, 7))
print(pendulum(3, 8))
print(pendulum(3, 9))
print(pendulum(3, 10))
print(pendulum(3, 11))
print(pendulum(3, 12))


# d = 5, t=7
#
def pendulum(d, t):
  # 1. get point on repeating pendulum swing positions
  t = t % (4 * d - 1)

  # 2. get point on sin wave t maps to
  return -d + abs(t - 2 * d)

# for i in range(25):
  # print(f"time: {i}, position: {pendulum(5, i)}")


'''
Follow-up:
What if the pendulum reduces by 1 distance per full swing? 
For example, for distance 3, the pendulum would go 
3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 0, -1, 0 
and then stay on 0 from this point forward.
'''


def dampeningPendulum(d, t):
  while d > 0 and t > 4 * d - 1:
    # 1. decrement t by time it took to go through full pendulum swing
    t -= 4 * d - 1

    # 2. decrement d by 1 (dampen)
    d -= 1

  if d == 0:
    return 0
  # find point on sin wave d points to
  return -d + abs(t - 2 * d)


for i in range(100):
  print(f"time: {i}, position: {dampeningPendulum(5, i)}")
