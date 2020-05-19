import unittest

from prime_generator import rwh_primes
from pyler import EulerProblem


class Problem0010(EulerProblem, unittest.TestCase):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
    the primes below two million.
    """

    problem_id = 10
    simple_input = 10
    simple_output = 17
    real_input = 2000000
    real_output = 142913828922

    def solver(self, input_val):
        return sum(rwh_primes(input_val))


if __name__ == "__main__":
    unittest.main()
