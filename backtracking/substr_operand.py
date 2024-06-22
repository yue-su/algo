'''
Generate all plus & minus expressions that equals target

Given a string that contains only digits from 0 to 9, and an integer value, *target*. Print all expressions which evaluate to *target* using the plus(+) and minus(-) binary operators between the digits.

You will likely need a helper function to recurse. You can use a loop within your recursive function because we're not monsters.
 

EXAMPLE(S)
generateExprs("123", 6) == ['1 + 2 + 3']
generateExprs("125", 7) == ['12 - 5']
generateExprs("420", 420) == ['420']
generateExprs("1210", 2) == ['1 + 2 - 1 + 0','1 + 2 - 1 - 0','12 - 10']
 

FUNCTION SIGNATURE
function generateExprs(seq, target) {
def generateExprs(seq: str, target: int) -> None:
'''

def generateExprs(sequence: str, target: int) -> list:
    """
    Generate all expressions that sum up to the target from the sequence.
    """
    def backtrack(start_index=0, current_sum=0, expression=[]):
        # Base case: if current sum equals target and we've used all digits
        if current_sum == target and start_index == len(sequence):
            results.append("".join(expression))
            return

        for i in range(start_index, len(sequence)):
            # Avoid numbers with leading zeros
            if sequence[start_index] == "0" and i > start_index:
                break

            current_number = int(sequence[start_index:i+1])

            if start_index == 0:
                # First number, just add it
                backtrack(i + 1, current_sum + current_number,
                          expression + [str(current_number)])
            else:
                # Add or subtract the current number and recurse
                backtrack(i + 1, current_sum + current_number,
                          expression + ["+", str(current_number)])
                backtrack(i + 1, current_sum - current_number,
                          expression + ["-", str(current_number)])

    results = []
    backtrack()
    return results


print(set(generateExprs("123", 6)) == {'1+2+3'})  # plus only

print(set(generateExprs("125", 7)) == {'12-5'})  # minus only
print(set(generateExprs("1236", 0)) == {'1+2+3-6'})  # mix

print(set(generateExprs("1235", -3)) == {'1-2+3-5'})  # mix
print(set(generateExprs("12036", 0)) == {'1+2+0+3-6', '1+2-0+3-6'})
print(set(generateExprs("12036", 18)) == {'1+20+3-6'})
print(set(generateExprs("1010", 9)) == {'10-1+0', '10-1-0'})
print(set(generateExprs("420", 420)) == {'420'})
print(set(generateExprs("1210", 2)) == {'12-10', '1+2-1+0', '1+2-1-0'})
