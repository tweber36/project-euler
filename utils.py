"""
    Toolbox of functions helpful to solve Project Euler problems.
"""


def fib(limit):
    """
    Returns all Fibonacci numbers up to limit.
    """
    yield 0
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b


def prime_factors(n):
    """
    Generator that returns all prime factors of a number.

    Every number n can at most have one prime factor greater than sqrt(n).
    If we, after dividing out some prime factor, calculate the square root of
    the remaining number, we can use that square root as upper limit for factor.
    If factor exceeds this square root we know the remaining number is prime.
    """
    if n % 2 == 0:
        while n % 2 == 0:
            yield 2
            n //= 2
    factor = 3
    max_factor = n ** 0.5
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            while n % factor == 0:
                yield factor
                n //= factor
            max_factor = n ** 0.5
        factor += 2
    if n > 1:
        yield n


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


def is_prime(n):
    """ Primality test of n by looking for divisors up to n / 2 """
    if n > 1:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        return True
    return False


def is_prime2(n):
    """
    Faster primality test looking for number in the form 6k +- 1
    and looking only up to the square root of n (because any factor after must be a
    multiple of smaller factor that has been already checked).
    """
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
