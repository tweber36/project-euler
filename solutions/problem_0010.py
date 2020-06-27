from math import sqrt

from pyler.pyler import EulerProblem
from utils.prime_generator import rwh_primes
from utils.primes import is_prime2


class Problem0010(EulerProblem):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
    the primes below two million.
    """

    problem_id = 10
    simple_input = 10
    simple_output = 17
    real_input = 2000000
    real_output = 142913828922

    @staticmethod
    def solver(input_val):
        """ Generate all primes below input_val and sums them """
        return sum(rwh_primes(input_val))

    @staticmethod
    def solver2(input_val):
        """ Check if numbers are primes up to input_val (naive and slow) """
        result = 5  # we know that 2 and 3 are prime
        n = 5
        while n <= input_val:
            if is_prime2(n):
                result += n
            n += 2
            if n <= input_val and is_prime2(n):
                result += n
            n += 4
        return result

    @staticmethod
    def solver3(input_val):
        """
        Using a sieve of Eratosthenes
        Similar to solver but using a list with input_val values: it takes more space and operations
        """
        limit = int(sqrt(input_val))
        sieve = [False] * (input_val + 1)
        for n in range(4, input_val + 1, 2):
            sieve[n] = True
        for n in range(3, limit + 1, 2):
            if not sieve[n]:
                for m in range(n * n, input_val + 1, 2 * n):
                    sieve[m] = True
        return sum(i for i in range(2, input_val + 1) if not sieve[i])

    @staticmethod
    def solver4(input_val):
        """
        Similar to solver3 but reduce the list with only odd values (half the space needed)
        and avoid some obvious crossing-outs
        """
        sieve_bound = (input_val + 1) // 2
        sieve = [False] * sieve_bound
        limit = (int(sqrt(input_val)) - 1) // 2
        for i in range(1, limit + 1):
            if not sieve[i]:
                for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                    sieve[j] = True
        return sum(2 * i + 1 for i in range(1, sieve_bound) if not sieve[i]) + 2


if __name__ == "__main__":
    import unittest
    unittest.main()
