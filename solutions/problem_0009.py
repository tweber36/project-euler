import unittest
from math import sqrt, gcd

from pyler import EulerProblem


class Problem0009(EulerProblem, unittest.TestCase):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,  a2 + b2 = c2 For example, 32 + 42 = 9 + 16 = 25 = 52. There exists
    exactly one Pythagorean triplet for which a + b + c = 1000.Find the product
    abc.
    """

    problem_id = 9
    simple_input = 12
    simple_output = 60
    real_input = 1000
    real_output = 31875000

    def solver(self, input_val):
        """
        This algorithm is sufficiently fast for small enough s,
        but it doesn’t scale well.
        If you multiply the value of s by a factor k, the span of each of the two loops
        is multiplied by the same factor and since the loops are nested, the number of
        cases to check is multiplied by k2. So if s is doubled, the programme takes
        approximately four times as long and increasing the perimeter s by a factor of
        10 increases the run time by a factor of approximately 100.
        """
        for a in range(1, int(input_val / 2)):
            for b in range(a + 1, int(input_val / 2) + 1):
                c = sqrt(a * a + b * b)
                if c.is_integer() and a + b + c == input_val:
                    return a * b * c
        return 0

    def solver2(self, input_val):
        """
        If a² + b² = c² and a + b + c = input_val
        then we can find b = input_val * (input_val/2-a) / (input_val-a)
        If you consider a < b, you can also find:
        a < input_val * (1 - sqrt(2) / 2)
        """
        for a in range(1, int(input_val * (1 - 1 / sqrt(2))) + 1):
            b = input_val * (input_val / 2 - a) / (input_val - a)
            if int(b) == b:
                return a * int(b) * (input_val - a - int(b))

    def solver3(self, input_val):
        """ See problem overview for details. """
        m_limit = int(sqrt(input_val / 2))
        for m in range(2, m_limit + 1):
            if (input_val / 2) % m == 0:  # input_val = 2 * m * (m + n) * d
                rest = (input_val / 2) / m
                while rest % 2 == 0:
                    rest /= 2
                if m % 2 == 1:  # Set start value for k = m + n
                    k = m + 2  # m < k < 2m
                else:
                    k = m + 1
                while k < 2 * m and k <= rest:
                    if rest % k == 0 and gcd(k, m) == 1:
                        d = (input_val / 2) / (k * m)
                        n = k - m
                        a = d * (m * m - n * n)
                        b = 2 * d * m * n
                        c = d * (m * m + n * n)
                        return a * b * c
                    k += 2


if __name__ == "__main__":
    unittest.main()
