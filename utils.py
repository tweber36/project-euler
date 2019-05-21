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