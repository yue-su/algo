
'''
Today, you will write a function that reverses a given number.
 

EXAMPLE(S)
Input: reverse(number: 123)
Output: 321

Input: reverse(number: 1548)
Output: 8451
 

FUNCTION SIGNATURE
func reverse(number: Int) -> Int
'''


# def reverse(number):
#     reversed_str = str(abs(number))[::-1]
#     nums = int(reversed_str)
#     return nums if number > 0 else nums * -1

def reverse(number: int) -> int:
    """
    Reverses the digits of an integer.
    
    Args:
        number (int): The integer to be reversed.
        
    Returns:
        int: The reversed integer.
    """
    is_negative = number < 0
    res = 0
    number = abs(number)
    while number:
        res = res * 10 + number % 10
        number //= 10
    return res * -1 if is_negative else res


print(reverse(123))
print(reverse(-123))
print(reverse(3567938709485702349485702438975))
