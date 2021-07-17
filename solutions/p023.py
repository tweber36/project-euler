import unittest

from pyler.pyler import EulerProblem
from utils.misc import sum_of_proper_divisors


class Problem0023(EulerProblem, unittest.TestCase):
    """
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number. A number n is called deficient if the sum of its proper divisors is
    less than n and it is called abundant if this sum exceeds n. As 12 is the
    smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
    can be written as the sum of two abundant numbers is 24. By mathematical
    analysis, it can be shown that all integers greater than 28123 can be
    written as the sum of two abundant numbers. However, this upper limit cannot
    be reduced any further by analysis even though it is known that the greatest
    number that cannot be expressed as the sum of two abundant numbers is less
    than this limit. Find the sum of all the positive integers which cannot be
    written as the sum of two abundant numbers.
    """

    problem_id = 23
    simple_input = 28123
    simple_output = 4179871
    real_input = 28123
    real_output = 4179871

    @staticmethod
    def solver(input_val):
        abundants = set()
        result = 0
        for n in range(1, input_val + 1):
            if sum_of_proper_divisors(n) > n:
                abundants.add(n)
            if not any((n - a in abundants) for a in abundants):
                result += n
        return result

    @staticmethod
    def solver2(input_val):
        """ First build the sum of divisors for all numbers and then look for non-abundants """
        sum_div = [1] * (input_val + 1)
        for i in range(2, int(input_val ** 0.5) + 1):
            sum_div[i * i] += i
            for k in range(i + 1, input_val // i + 1):
                sum_div[k * i] += k + i

        abundants, result = set(), 0
        for n in range(1, input_val + 1):
            if sum_div[n] > n:
                abundants.add(n)
            if not any((n - a in abundants) for a in abundants):
                result += n
        return result


if __name__ == "__main__":
    unittest.main()
