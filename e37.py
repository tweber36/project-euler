from itertools import chain


def build_primes(n):
    """Return a set with primes up to n."""
    not_primes = set()
    for i in range(2, n):
        if i in not_primes:
            continue
        multiplier = i
        while i * multiplier <= n:
            not_primes.add(i * multiplier)
            multiplier += 1

    return set(range(2, n)).difference(not_primes)


def is_truncatable(n):
    """
    Return if a number is truncatable from the right and the left.
    Ex: 3797 is prime, so are 797, 97, 7 and 379, 37, 3.
    """
    n = str(n)
    n_parts = set(chain.from_iterable([[n[i:], n[:-i]] for i in range(1, len(n))]))
    n_parts.add(n)

    for number in n_parts:
        if int(number) not in primes:
            return False
    return True

n = 1000000
primes = build_primes(n)

truncatables = set()
for x in primes:
    if len(truncatables) >= 11:
        break
    if is_truncatable(x) and x > 10:
        truncatables.add(x)

print(sum(truncatables))
