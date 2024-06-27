class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = None
        used = set()
        length = 2 ** n

        def flipbit(num, i):
            return num ^ (1 << i)

        def helper(start=0, path=[]):
            nonlocal res

            if res:
                return

            if len(path) == length:
                res = path[:]
                return

            if start in used:
                return

            path.append(start)
            used.add(start)

            for i in range(n):
                num = flipbit(start, i)
                helper(num, path)

            used.remove(start)

        helper()

        return res



def grayCode(n: int) -> list[int]:
    """
    Generates a Gray code sequence for a given number of bits.

    Args:
        n (int): The number of bits in each code of the sequence.

    Returns:
        list[int]: A list containing the Gray code sequence.
    """
    total_numbers = 2 ** n
    gray_codes = [(i ^ (i >> 1)) for i in range(total_numbers)]
    return gray_codes


print(grayCode(2))
print(grayCode(4))
print(grayCode(5))
