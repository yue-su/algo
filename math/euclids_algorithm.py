def euclidGCD(a, b):
    if a == 0:
        return b
    return euclidGCD(b % a, a)


print(euclidGCD(9, 27) == 9)
print(euclidGCD(27, 9) == 9)
print(euclidGCD(3, 1) == 1)
print(euclidGCD(50, 1) == 1)
print(euclidGCD(50, 2) == 2)
print(euclidGCD(50, 4) == 2)
print(euclidGCD(100, 50) == 50)
print(euclidGCD(23, 23) == 23)
print(euclidGCD(10, 10) == 10)
print(euclidGCD(31, 19) == 1)
print(euclidGCD(1, 1) == 1)
