'''
Question : 

Find the number of circular primes less than or equal to upper bound.

The number 197 is called a circular prime because all rotations of the digits:
197, 971, and 719 are themselves prime.

There are 13 circular primes between 2 and 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97
 

EXAMPLE(S)
countCircularPrimes(100) == 13
 
Edge cases/Assumptions/Observations:
- lowerBound = 2 and upperBound will be provided as an input
- Values are integers
find all non-primes between lowerBound and upperBound

Approach : 
- Using Sieve of Eratosthenes - more efficient
 - we need to remove non-primes in the range (lower, upper)
 - use string manipulation for rotating number
 - we need to see if circular rotations are also prime 
 - tweak upper bound by checking number of digits in upperbound
  - we need to tweak upperbound 
  


FUNCTION SIGNATURE
function countCircularPrimes(upperBound) {
def countCircularPrimes(upperBound: int) -> int:


'''


def countCircularPrimes(upperBound: int) -> int:
  num_of_digits = len(str(upperBound))
  digits = ["9"] * num_of_digits
  upper = int("".join(digits))

  primes = sieveOfEratosthenes(upper)
  res = 0

  for prime in range(upperBound+1):
    rotations = getAllRotations(prime)
    allPrimes = True
    for num in rotations:  # checking all rotations here
      if num not in primes:
        allPrimes = False
        break
    if allPrimes:
      res += 1

  return res


def getAllRotations(prime):
 # return set of all rotations
  nums = [c for c in str(prime)]
  rotations = set()
  for i in range(len(nums)):
    nums.append(nums.pop(0))
    rotations.add(int("".join(nums)))
  return rotations


def sieveOfEratosthenes(upper):
  primes = [True] * (upper + 1)
  primes[0] = False
  primes[1] = False

  p = 2

  while p <= upper:
    if primes[p]:
      for i in range(p+1, upper + 1):
        if i % p == 0:
          primes[i] = False
    p += 1

  return [num for num in range(upper+1) if primes[num]]


print(countCircularPrimes(100))
