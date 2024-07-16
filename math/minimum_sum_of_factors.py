
/*
'''
Given a positive integer N, calculate the smallest possible sum by adding together the set of factors that multiply to produce N.


EXAMPLE(S)
Input: 12
Output: 7
Explanation: There are 4 ways to factorize 12 and the sum of factors.
12 = 12 * 1 => 12 + 1 = 13
12 = 2 * 6 becomes 2 + 6 = 8
12 = 3 * 4 becomes 3 + 4 = 7
12 = 2 * 2 * 3 becomes 2 + 2 + 3 = 7

Input: 105
Output: 15

3 * 5 * 7 = 105
3 + 5 + 7 = 15


FUNCTION SIGNATURE
func minSumOfFactors(number: Int) -> Int
'''

1. clarifications:
  input: positive integer
  outout: integer

2. brainstorming
12:
  1 -> 1 + 12
  2 -> 2 + 6 = 8
  3 -> 3 + 4 = 7
  input ^ 0.5

3. approach

  remainder = number % i
   if remainder == 0:
        res = number // i
        sum = i + res
        while (res != 0){
            res
        }

    ex 15 -> 3 -> 15/3 num 5

    initial = 2
    while number != 1
       res = number / initial -> 5
        if res is a float:
          initial++
        else:
          sum += inital -> 3
          number = res -> 5

    if(1prime )
    sum += number

    else return number
*/

// function minSumOfFactors(number) {
    // let sum = 0
    // let initial = 2

    // while (number != 1) {

        //     let res = number / initial
        //     if (Number.isInteger(res)) {
        //       sum += initial
        //       number = res
        //     } else {
        //       initial += 1
        //     }
        //   }

    // return sum

    //}

// function isPrime(n) {
    //   for (let i = 2
i <= Math.sqrt(n)
i++) {
    //     if (n % i == = 0) {
    // return false;
    //}
    //}
    // return true;
    //}

// function minSumOfFactors(num) {
    //   let res = 0

    // // use helper function to find prime numbers
    // if (isPrime(num)) {
    //     return num + 1
        //   }

    // // num is not prime
    // let i = 2;
    // while (i * i <= num) {
        //     if (num % i == = 0) {
    // res += i;
    // num = Math.floor(num / i);
    //} else {
    // i++;
    //}
        //   }

    // if (num > 1) {
        //     res += num;
        //   }

    // return res;
    //}

function minSumOfFactors(num) {
    if (num == = 1) {
      return 2
  }

  let counter = 0
  let divider = 2;
  let res = 0;

  while (num !== 1) {
      if (num / divider == = Math.floor(num / divider)) {
        num = Math.floor(num / divider);
        res += divider;
        counter += 1;
    } else {
        divider += 1;
    }
  }

  if (counter === 1) {
      res += num;
  }

  return res;
}

console.log(minSumOfFactors(6))
console.log(minSumOfFactors(10))
console.log(minSumOfFactors(15))
console.log(minSumOfFactors(12))
console.log(minSumOfFactors(31))
