import unittest

from pyler import EulerProblem


class Problem0006(EulerProblem, unittest.TestCase):
    """
    The sum of the squares of the first ten natural numbers is, 12 + 22 + ... +
    102 = 385 The square of the sum of the first ten natural numbers is, (1 + 2
    + ... + 10)2 = 552 = 3025 Hence the difference between the sum of the
    squares of the first ten natural numbers and the square of the sum is 3025 −
    385 = 2640. Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    """

    problem_id = 6
    simple_input = 10
    simple_output = 2640
    real_input = 100
    real_output = 25164150

    def solver(self, input_val):
        sum_square = sum(x ** 2 for x in range(1, input_val + 1))
        square_sum = sum(x for x in range(1, input_val + 1)) ** 2

        return square_sum - sum_square

    def solver2(self, input_val):
        """
        For numbers below n:
        Sum of the squares = n(n+1)(2n+1) / 6
        Square of the sum = n²(n+1)² / 4
        Difference is = (n^3-n)(3n+2) / 12
        """
        return int((input_val ** 3 - input_val) * (3 * input_val + 2) / 12)


if __name__ == "__main__":
    unittest.main()
