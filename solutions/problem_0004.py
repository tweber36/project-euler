import unittest

from pyler import EulerProblem


class Problem0004(EulerProblem, unittest.TestCase):
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
    palindrome made from the product of two 3-digit numbers.
    """

    problem_id = 4
    simple_input = 2
    simple_output = 9009
    real_input = 3
    real_output = 906609

    def solver(self, input_val):
        """
        Let our palindrome be P = ab with a and b the input_val-digit numbers.
        If a and b are input_val-digits long then they must lie between
        10^(input_val-1) and 10^(input_val) - 1.
        """
        max_pal = 0
        for a in range(10 ** (input_val - 1), 10 ** input_val):
            for b in range(10 ** (input_val - 1), 10 ** input_val):
                if str(a * b) == str(a * b)[::-1] and a * b > max_pal:
                    max_pal = a * b
        return max_pal

    def solver2(self, input_val):
        """
        To stop checking many numbers multiple times we can assume a <= b.
        This roughly halves the number of calculations needed.
        """
        max_pal = 0
        for a in range(10 ** (input_val - 1), 10 ** input_val):
            for b in range(a, 10 ** input_val):
                if str(a * b) == str(a * b)[::-1] and a * b > max_pal:
                    max_pal = a * b
        return max_pal

    def solver3(self, input_val):
        """
        Instead of going upwards, we consider counting downwards and stop checking
        a and b that would be too small to improve upon the largest palindrome found
        so far.
        This is way faster (about 80 times).
        """
        max_pal = 0
        for a in range(10 ** input_val - 1, 10 ** (input_val - 1) - 1, -1):
            for b in range(10 ** input_val - 1, a - 1, -1):
                if a * b <= max_pal:
                    break
                if str(a * b) == str(a * b)[::-1] and a * b > max_pal:
                    max_pal = a * b
        return max_pal

    def solver4(self, input_val):
        """
        Consider the digits of P - let them be x, y and z.
        P must be at least 6 digits long since the palindrome 111111 = 143x777 -
        the product of two 3-digit integers.
        Since P is palindromic:
        P = 100000x + 10000y + 1000z + 100z + 10y + x
        P = 11(9091x + 910y + 100z)
        Since 11 is prime, either a or b must have a factor of 11.
        So if a is not divisible by 11, then we know b must be.
        """
        max_pal = 0
        for a in range(10 ** input_val - 1, 10 ** (input_val - 1) - 1, -1):
            if a % 11 == 0:
                b_start, b_step = 10 ** input_val - 1, 1
            else:
                # b_start = largest number less than 10 ** input_val - 1
                # and divisible by 11
                b_start, b_step = 11 * (10 ** input_val - 1) // 11, 11

            for b in range(b_start, a - 1, -b_step):
                if a * b <= max_pal:
                    break
                if str(a * b) == str(a * b)[::-1] and a * b > max_pal:
                    max_pal = a * b

        return max_pal


if __name__ == "__main__":
    unittest.main()
