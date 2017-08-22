"""
Same problem - different proof.
Noting that the leftmost digit must be prime: {2, 3, 5, 7}
The rightmost digit must be {3, 7} because numbers > 9 ending in {0, 2, 5}
can never be prime.
Finally the middle digits cannot be odd and cannot be {0, 2, 5} which leaves
{1, 3, 7, 9}
"""
from collections import deque
from math import sqrt


def is_prime(n):
    if n < 0:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_left_truncatable(n):
    modulus = 10
    while modulus < n:
        if not is_prime(n % modulus):
            return False
        modulus *= 10
    return True


total = 0
search_queue = deque([2, 3, 5, 7])
while search_queue:
    head = search_queue.popleft()
    for tail in [1, 3, 7, 9]:
        candidate = 10*head+tail
        if not is_prime(candidate):
            continue
        search_queue.append(candidate)
        if (candidate % 10 not in (1, 9)) and is_left_truncatable(candidate):
            total += candidate

print(total)
