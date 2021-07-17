from math import log

from pyler.pyler import EulerProblem
from utils.prime_generator import rwh_primes
from utils.primes import is_prime2


class Problem0007(EulerProblem):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13. What is the 10 001st prime number?
    """

    problem_id = 7
    simple_input = 6
    simple_output = 13
    real_input = 10001
    real_output = 104743

    @staticmethod
    def solver(input_val):
        """
        Some useful facts:
        1 is not a prime.
        All primes except 2 are odd.
        All primes greater than 3 can be written in the form 6k+/-1.
        Any number n can have only one primefactor greater than n .
        The consequence for primality testing of a number n is:
        if we cannot find a number f less than or equal n that divides n
        then n is prime: the only primefactor of n is n itself
        """

        count = 1  # 2 is prime
        candidate = 1
        while count < input_val:
            candidate += 2
            if is_prime2(candidate):
                count += 1

        return candidate

    @staticmethod
    def solver2(input_val):
        """
        If p(n) is the n-th prime number, we know (Rosser, 1941) that an upper bound
        for n >= 6 is: n * ln( n * ln(n))
        We generate primes up to that upper bound and then return the n-th prime.
        It is way faster than generating all primes until we have n primes.
        """
        if input_val >= 6:
            upper_bound = input_val * log(input_val * log(input_val))
            primes = rwh_primes(int(upper_bound))
            return primes[input_val - 1]
        else:
            return [2, 3, 5, 7, 11][input_val - 1]


if __name__ == "__main__":
    import unittest
    unittest.main()
