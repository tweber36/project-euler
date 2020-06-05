
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
