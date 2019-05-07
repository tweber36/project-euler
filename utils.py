"""
    Toolbox of functions helpful to solve Project Euler problems.
"""


def fib(limit):
    """
    Returns all Fibonacci numbers up to limit.
    See problem 2 for details.
    """
    yield 0
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b


def prime_factors(n):
    """
    Generator that returns all prime factors of a number.
    See problem 3 for details.
    """
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        yield 2
    factor = 3
    max_factor = n ** 0.5
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            while n % factor == 0:
                n //= factor
            max_factor = n ** 0.5
            yield factor
        factor += 2
    yield n


def build_n_primes(n):
    """Build the first n prime numbers."""
    primes = [2]
    i = 3
    while len(primes) < n:
        is_prime = True
        root_square_limit = i ** 0.5
        for p in primes:
            if p > root_square_limit:
                break
            elif i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes


def sieve_eratosthene(n):
    """ Returns a set with primes up to n."""
    not_primes = set()
    for i in range(2, n):
        if i in not_primes:
            continue
        multiplier = i
        while i * multiplier <= n:
            not_primes.add(i * multiplier)
            multiplier += 1

    return set(range(2, n)).difference(not_primes)


def primes_generator(n):
    """ Returns a generator of primes < n."""
    a = [True] * n
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for x in range(i * i, n, i):
                a[x] = False


def primes_list(n):
    # https://stackoverflow.com/questions/2068372
    # /fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of primes < n."""
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if sieve[i]]
