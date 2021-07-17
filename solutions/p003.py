from pyler.pyler import EulerProblem
from utils.primes import prime_factors


class Problem0003(EulerProblem):
    """
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
    factor of the number 600851475143 ?
    """

    problem_id = 3
    simple_input = 13195
    simple_output = 29
    real_input = 600851475143
    real_output = 6857

    @staticmethod
    def solver(input_val):
        """
        Naive solution testing all numbers to see if they are a prime factor.
        """
        n = input_val
        factor = 2
        last_factor = 1
        while n > 1:
            if n % factor == 0:
                last_factor = factor
                while n % factor == 0:
                    n //= factor
            factor += 1
        return last_factor

    @staticmethod
    def solver2(input_val):
        """
        A bit less naive, testing 2 and then only odd numbers.
        """
        n = input_val
        last_factor = 1
        if n % 2 == 0:
            last_factor = 2
            while n % 2 == 0:
                n //= 2
        factor = 3
        while n > 1:
            if n % factor == 0:
                last_factor = factor
                while n % factor == 0:
                    n //= factor
            factor += 2
        return last_factor

    @staticmethod
    def solver3(input_val):
        """
        Every number n can at most have one prime factor greater than sqrt(n).
        If we, after dividing out some prime factor, calculate the square root of
        the remaining number, we can use that square root as upper limit for factor.
        If factor exceeds this square root we know the remaining number is prime.
        """
        n = input_val
        last_factor = 1
        if n % 2 == 0:
            last_factor = 2
            while n % 2 == 0:
                n //= 2
        factor = 3
        max_factor = n ** 0.5
        while n > 1 and factor <= max_factor:
            if n % factor == 0:
                last_factor = factor
                while n % factor == 0:
                    n //= factor
                max_factor = n ** 0.5
            factor += 2
        if n == 1:
            return last_factor
        return n

    @staticmethod
    def solver4(input_val):
        """ Same but using a generator that returns all prime factors. """
        return list(prime_factors(input_val))[-1]


if __name__ == "__main__":
    import unittest
    unittest.main()
