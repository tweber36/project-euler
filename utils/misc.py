
def fib(limit):
    """
    Returns all Fibonacci numbers up to limit.
    """
    yield 0
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b


def sum_of_proper_divisors(n):
    """
    Return the sum of proper divisors of n.

    Ex: if n = 12, it proper divisors are 1, 2, 3, 4, 6 and the sum is 16
    Solution that uses the two facts:
    1. for every divisor d, n / d is also a divisor (they come by pair except
     for a perfect square)
    2. Odd numbers cannot have even divisors
    Three solutions were tested in problem 21, this was the fastest.
    """
    if n == 1:
        return 1
    limit = int(n ** 0.5)
    if limit * limit == n:
        answer = 1 + limit
        limit -= 1
    else:
        answer = 1
    divisor_ini, step = (3, 2) if (n & 1) else (2, 1)
    answer += sum(
        divisor + n // divisor
        for divisor in range(divisor_ini, limit + 1, step)
        if n % divisor == 0
    )
    return answer
