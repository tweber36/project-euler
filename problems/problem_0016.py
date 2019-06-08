import unittest
from pyler import EulerProblem


class Problem0016(EulerProblem, unittest.TestCase):
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is the
    sum of the digits of the number 2^1000?
    """

    problem_id = 16
    simple_input = 15
    simple_output = 26
    real_input = 1000
    real_output = 1366

    def solver(self, input_val):
        return sum(map(int, str(2 ** input_val)))

    def solver2(self, input_val):
        return sum(int(digit) for digit in str(2 ** input_val))

    def solver3(self, input_val):
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        return sum_digits(2 ** input_val)

    def solver4(self, input_val):
        def sum_digits(n):
            s = 0
            while n:
                n, remainder = divmod(n, 10)
                s += remainder
            return s

        return sum_digits(2 ** input_val)

    def solver5(self, input_val):
        def sum_digits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r

        return sum_digits(2 ** input_val)


if __name__ == "__main__":
    unittest.main()
