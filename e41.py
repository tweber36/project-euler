"""
We shall say that an n-digit number is pandigital if
it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
--------------------------------------------------
Testing with 7-digits first and then going down until a solution is found
Not 8 because 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36 can be divided by 3
Not 9 because 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 can be divided by 3
so all 8-digits and 9-digits pandigital numbers are not primes.
"""
from math import sqrt
from itertools import permutations


def is_prime(n):
    if n < 0:
        return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number_of_digits = 7
    max_pandi_number = 0
    while number_of_digits > 0:
        print("Testing with {} digits".format(number_of_digits))
        digits = [x for x in range(1, number_of_digits+1)]
        for shuffle in permutations(digits):
            number_to_test = int("".join([str(x) for x in shuffle]))
            if number_to_test > max_pandi_number and is_prime(number_to_test):
                max_pandi_number = number_to_test
        if max_pandi_number > 0:
            print(max_pandi_number)
            break
        number_of_digits -= 1
