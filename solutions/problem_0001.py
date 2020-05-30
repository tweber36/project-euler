import unittest

from pyler.pyler import EulerProblem


class Problem0001(EulerProblem, unittest.TestCase):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
    multiples of 3 or 5 below 1000.
    """

    problem_id = 1
    simple_input = 9
    simple_output = 23
    real_input = 999
    real_output = 233168

    def solver(self, input_val):
        """
        Sum of numbers divisible by 3 (=3+6+9+..+999=3*(1+2+3+..+333)) +
        sum of numbers divisble by 5 (=5+10+..+995=5*(1+2+..+199)) -
        sum of numbers divisible by 15 (=15+30+..+990=15*(1+2+..+66))
        """
        return (
            3 * (input_val // 3 * (input_val // 3 + 1) // 2)
            + 5 * (input_val // 5 * (input_val // 5 + 1) // 2)
            - 15 * (input_val // 15 * (input_val // 15 + 1) // 2)
        )

    def solver2(self, input_val):
        """ One-liner but more than 100 times slower"""
        return sum(x for x in range(input_val + 1) if x % 3 == 0 or x % 5 == 0)


if __name__ == "__main__":
    unittest.main()
