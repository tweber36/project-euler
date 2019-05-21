"""
Module that implements various methods for generating prime numbers
up to a certain number.
Based on:
https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
"""

from math import sqrt, ceil
import numpy as np


def sieve_of_eratosthenes(n):
    """
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Two optimizations: start marking off numbers at the square of a prime (start_index)
    and stop if we go above the square root of n.
    """
    if n < 2:
        return []
    sieve = list(range(3, n + 1, 2))  # all odd's from 3 to n
    sieve_len = len(sieve)
    for candidate in sieve:
        if candidate != 0:
            # -2 because we start at 3, not 1 and //2 because we keep only odd's
            start_index = (candidate * candidate - 2) // 2

            if start_index >= sieve_len:
                break
            sieve[start_index::candidate] = [0] * int(
                ceil((sieve_len - start_index) / candidate)
            )
    return [2] + [elt for elt in sieve if elt]


def sieve_of_sundaram(n):
    """ https://en.wikipedia.org/wiki/Sieve_of_Sundaram """
    n_new = (n - 2) // 2
    numbers = list(range(1, n_new + 1))
    initial_j = 4
    for i in range(1, n_new + 1):
        for j in range(initial_j, n_new + 1, 2 * i + 1):
            numbers[j - 1] = 0
        initial_j += 4 * (i + 1)

        if initial_j > n_new:
            return [2] + [2 * elt + 1 for elt in numbers if elt]


def sieve_of_atkin(n_max):
    """
    Code based on: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
    """
    primes = [2, 3, 5]
    if n_max <= 5:
        return primes[: int(ceil(n_max / 2))]

    sieve = [False] * ((n_max - 1) // 2 + 1)  # keep only odd's

    # Case: 4x² + y² = n
    x_max = int(sqrt((n_max - 1) / 4.0))
    for x in range(1, x_max + 1):
        y_start = int(sqrt(n_max - 4 * x * x))  # y_max
        n = 4 * x * x + y_start * y_start
        if not (n & 1):  # if n is even
            y_start -= 1
            n -= 2 * y_start + 1
        for y in range(y_start, 0, -2):
            if n % 60 in (1, 13, 17, 29, 37, 41, 49, 53):
                sieve[n >> 1] = not sieve[n >> 1]
            n -= 4 * (y - 1)

    # Case: 3x² + y² = n
    x_max = int(sqrt((n_max - 1) / 3.0))
    for x in range(1, x_max + 1):
        y_start = int(sqrt(n_max - 3 * x * x))
        n = 3 * x * x + y_start * y_start
        if not (n & 1):
            y_start -= 1
            n -= 2 * y_start + 1
        for y in range(y_start, 0, -2):
            if n % 60 in (7, 19, 31, 43):
                sieve[n >> 1] = not sieve[n >> 1]
            n -= 4 * (y - 1)

    # Case: 3x² - y² = n, x > y
    x_max = int(sqrt(n_max / 2))
    for x in range(2, x_max + 1):
        y_start = x - 1
        n = 3 * x * x - y_start * y_start
        for y in range(y_start, 0, -2):
            if n > n_max:
                break
            if n % 60 in (11, 23, 47, 59):
                sieve[n >> 1] = not sieve[n >> 1]
            n += 4 * (y - 1)

    # Mark off squares of primes
    for n in range(5, int(sqrt(n_max)) + 1, 2):
        if sieve[n >> 1]:
            primes.append(n)
            n2 = n * n
            for k in range(n2, n_max, 2 * n2):
                sieve[k >> 1] = False

    s = int(sqrt(n_max)) + 1
    if s % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, n_max, 2) if sieve[i >> 1]])
    return primes


def rwh_primes(n):
    """ Variant of sieve of Eratosthenes but more pythonic """
    sieve = [True] * (n + 1)
    for i in range(3, int(sqrt(n + 1)) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i) // (2 * i) + 1)
    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]


def rwh_primes1(n):
    """ Same but with half sieve """
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(sqrt(n + 1)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = [False] * ((n - i * i) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, (n + 1) // 2) if sieve[i]]


def rwh_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n + 1) % 6 > 1
    n = {0: n + 1, 1: n, 2: n + 5, 3: n + 4, 4: n + 3, 5: n + 2}[(n + 1) % 6]
    sieve = [True] * ((n + 1) // 3)
    sieve[0] = False
    for i in range(int(sqrt(n + 1)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3) :: 2 * k] = [False] * (
                ((n + 1) // 6 - (k * k) // 6 - 1) // k + 1
            )
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3 :: 2 * k] = [False] * (
                ((n + 1) // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1
            )
    return [2, 3] + [
        3 * i + 1 | 1 for i in range(1, (n + 1) // 3 - correction) if sieve[i]
    ]


def sieve_wheel_30(N):
    """ Returns a list of primes <= N using wheel criterion 2*3*5 = 30 """

    __smallp = (
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    )

    wheel = (2, 3, 5)
    const = 30
    if N < 2:
        return []
    if N <= const:
        pos = 0
        while __smallp[pos] <= N:
            pos += 1
        return list(__smallp[:pos])
    # make the offsets list
    offsets = (7, 11, 13, 17, 19, 23, 29, 1)
    # prepare the list
    p = [2, 3, 5]
    dim = 2 + N // const
    tk1 = [True] * dim
    tk7 = [True] * dim
    tk11 = [True] * dim
    tk13 = [True] * dim
    tk17 = [True] * dim
    tk19 = [True] * dim
    tk23 = [True] * dim
    tk29 = [True] * dim
    tk1[0] = False
    # help dictionary d
    # d[a , b] = c  ==> if I want to find the smallest useful multiple of (30*pos)+a
    # on tkc, then I need the index given by the product of [(30*pos)+a][(30*pos)+b]
    # in general. If b < a, I need [(30*pos)+a][(30*(pos+1))+b]
    d = {}
    for x in offsets:
        for y in offsets:
            res = (x * y) % const
            if res in offsets:
                d[(x, res)] = y
    # another help dictionary: gives tkx calling tmptk[x]
    tmptk = {1: tk1, 7: tk7, 11: tk11, 13: tk13, 17: tk17, 19: tk19, 23: tk23, 29: tk29}
    pos, prime, lastadded, stop = 0, 0, 0, int(ceil(sqrt(N)))
    # inner functions definition
    def del_mult(tk, start, step):
        for k in xrange(start, len(tk), step):
            tk[k] = False

    # end of inner functions definition
    cpos = const * pos
    while prime < stop:
        # 30k + 7
        if tk7[pos]:
            prime = cpos + 7
            p.append(prime)
            lastadded = 7
            for off in offsets:
                tmp = d[(7, off)]
                start = (
                    (pos + prime)
                    if off == 7
                    else (prime * (const * (pos + 1 if tmp < 7 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 11
        if tk11[pos]:
            prime = cpos + 11
            p.append(prime)
            lastadded = 11
            for off in offsets:
                tmp = d[(11, off)]
                start = (
                    (pos + prime)
                    if off == 11
                    else (prime * (const * (pos + 1 if tmp < 11 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 13
        if tk13[pos]:
            prime = cpos + 13
            p.append(prime)
            lastadded = 13
            for off in offsets:
                tmp = d[(13, off)]
                start = (
                    (pos + prime)
                    if off == 13
                    else (prime * (const * (pos + 1 if tmp < 13 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 17
        if tk17[pos]:
            prime = cpos + 17
            p.append(prime)
            lastadded = 17
            for off in offsets:
                tmp = d[(17, off)]
                start = (
                    (pos + prime)
                    if off == 17
                    else (prime * (const * (pos + 1 if tmp < 17 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 19
        if tk19[pos]:
            prime = cpos + 19
            p.append(prime)
            lastadded = 19
            for off in offsets:
                tmp = d[(19, off)]
                start = (
                    (pos + prime)
                    if off == 19
                    else (prime * (const * (pos + 1 if tmp < 19 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 23
        if tk23[pos]:
            prime = cpos + 23
            p.append(prime)
            lastadded = 23
            for off in offsets:
                tmp = d[(23, off)]
                start = (
                    (pos + prime)
                    if off == 23
                    else (prime * (const * (pos + 1 if tmp < 23 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 29
        if tk29[pos]:
            prime = cpos + 29
            p.append(prime)
            lastadded = 29
            for off in offsets:
                tmp = d[(29, off)]
                start = (
                    (pos + prime)
                    if off == 29
                    else (prime * (const * (pos + 1 if tmp < 29 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # now we go back to top tk1, so we need to increase pos by 1
        pos += 1
        cpos = const * pos
        # 30k + 1
        if tk1[pos]:
            prime = cpos + 1
            p.append(prime)
            lastadded = 1
            for off in offsets:
                tmp = d[(1, off)]
                start = (
                    (pos + prime)
                    if off == 1
                    else (prime * (const * pos + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
    # time to add remaining primes
    # if lastadded == 1, remove last element and start adding them from tk1
    # this way we don't need an "if" within the last while
    if lastadded == 1:
        p.pop()
    # now complete for every other possible prime
    while pos < len(tk1):
        cpos = const * pos
        if tk1[pos]:
            p.append(cpos + 1)
        if tk7[pos]:
            p.append(cpos + 7)
        if tk11[pos]:
            p.append(cpos + 11)
        if tk13[pos]:
            p.append(cpos + 13)
        if tk17[pos]:
            p.append(cpos + 17)
        if tk19[pos]:
            p.append(cpos + 19)
        if tk23[pos]:
            p.append(cpos + 23)
        if tk29[pos]:
            p.append(cpos + 29)
        pos += 1
    # remove exceeding if present
    pos = len(p) - 1
    while p[pos] > N:
        pos -= 1
    if pos < len(p) - 1:
        del p[pos + 1 :]
    # return p list
    return p


################################################################################
# Using Numpy:
def ambi_sieve(n):
    # http://tommih.blogspot.com/2009/04/fast-prime-number-generator.html
    s = np.arange(3, n + 1, 2)
    for m in range(3, int(sqrt(n + 1)) + 1, 2):
        if s[(m - 3) // 2]:
            s[(m * m - 3) // 2 :: m] = 0
    return list(np.r_[2, s[s > 0]])


def primesfrom3to(n):
    """ Returns a array of primes, p <= n """
    assert n >= 2
    sieve = np.ones((n + 1) // 2, dtype=np.bool)
    for i in range(3, int(sqrt(n + 1)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = False
    return list(np.r_[2, 2 * np.nonzero(sieve)[0][1::] + 1])


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p <= n """
    sieve = np.ones((n + 1) // 3 + ((n + 1) % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(sqrt(n + 1)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3) :: 2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3 :: 2 * k] = False
    return list(np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)])


if __name__ == "__main__":
    import timeit

    methods = [
        "sieve_of_eratosthenes",
        "sieve_of_sundaram",
        "sieve_of_atkin",
        "rwh_primes",
        "rwh_primes1",
        "rwh_primes2",
        "primesfrom3to",
        "primesfrom2to",
        "ambi_sieve"
    ]

    for method in methods:
        loops, time_tot = timeit.Timer(
            f"{method}(1000000)", setup=f"from prime_generator import {method}"
        ).autorange()
        print(f"{method}: {time_tot / loops * 1000:.2f}ms per loop")
        print(f"{locals()[method](97)}")
