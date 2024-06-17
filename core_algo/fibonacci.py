def fib(k: int) -> int:

    # Write your code here.
    if k <= 1:
        return 1

    pre = cur = 1
    for _ in range(2, k+1):
        pre, cur = cur, pre+cur

    return cur


# Test Cases
print(fib(0))  # 1
print(fib(5))  # 8
print(fib(11))  # 144
