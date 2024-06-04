'''
Imagine you work at a company like Google, Facebook, OpenAI or any other company with a major online service. Millions to potentially billions of people are counting on your service to be up and running and accessible. It's an interesting thought exercise just to estimate the number of individual HTTP requests made to one of these services in a single day or even per second!

One key component of these systems is to ensure that no user can consume more than their fair share of the system's capacity to respond to these requests. This is accomplished via rate limiting, restricting the rate at which any single user can make requests.

The goal of the rate limiter is to make sure humans who use the system are able to do so, while scripts and other automatic processes might be slowed down or even denied access to reserve enough capacity for real users.

A rate-limiting algorithm (or heuristic) tracks the rate of requests from any single user and decides to allow the request through or deny it.

Work with your fellows to derive, implement, and test multiple rate-limiting algorithms. Discuss the pros and cons of each along the way.

Design these rate limiters in a testable way. We recommend passing in the current time as an argument along with the user id. The time can be a number representing seconds or milliseconds.
 

EXAMPLE(S)
console.log(isRateLimited('spammy', 1)); // false, not limited, allowed through
for (let i = 0; i < 1000; i++) isRateLimited('spammy', 1); // make a lot of calls at the same time
console.log(isRateLimited('spammy', 1)); // true, limiter kicks in, request is denied
console.log(isRateLimited('other', 1)); // false, this other user is allowed through!

// simulate waiting a long time by increasing the current time
console.log(isRateLimited('spammy', 1000000)); // false

-> each user can request 3 times a minute, return False
-> if a user goes over the limit within the minute, return True


[request1, request2, request3] request4
                      

spammy, 1
spammy, 1
spammy, 1
spammy, 30

{spammy: [timestamp: count]}
 

FUNCTION SIGNATURE
function isRateLimited(userID: string, currentTime: number): boolean

spammy, 1
'''


storage = {}

def isRateLimited(user_id, current_time):
  if user_id not in storage:
    storage[user_id] = [0, current_time]

  user_info = storage[user_id]
 
  if current_time - user_info[1] <= 60 and user_info[0] < 3:
    user_info[0] += 1
    return False

  elif current_time - user_info[1] > 60:
    user_info[0] = 1 # need to set to 1, we set it to 0 before
    user_info[1] = current_time
    return False

  else:
    return True

    

  

print(isRateLimited("spammy", 1)) #F
print(isRateLimited("spammy", 1)) #F
print(isRateLimited("spammy", 1)) #F
print(isRateLimited("spammy", 1)) #T
print(isRateLimited("spammy", 62)) #F
print(isRateLimited("spammy", 62)) #F
print(isRateLimited("spammy", 62)) #F
print(isRateLimited("spammy", 62)) #T
print(isRateLimited("spammy", 123)) #F







