import unittest
from itertools import permutations
from math import factorial, ceil

from pyler import EulerProblem


class Problem0024(EulerProblem, unittest.TestCase):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
    are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120 
     201   210 What is the millionth lexicographic permutation of the digits 0,
    1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    problem_id = 24
    simple_input = (3, 5)
    simple_output = 201
    real_input = (10, 1000000)
    real_output = 2783915460

    def solver(self, input_val):
        digits, perm_limit = range(input_val[0]), input_val[1]
        perms = list(permutations(digits))
        return int("".join(map(str, perms[perm_limit - 1])))

    def solver2(self, input_val):
        """
        Here's a cool way to solve this problem. Figure out the problem digit by digit.
        First the sorted digits are [0,1,2,3,4,5,6,7,8,9] so let's figure out where
        the millionth permutation will lie. This is easy to figure out since the
        permutations are sorted. We know that in this sorted permutation list, we will
        have 10! = 3628800 permutations and they will appear as follows: 362880
        permutation with '0' as the first digit, 362880 with '1' as the first digit,
        362880 with '2' as the first digit, and so on for a total of 362880*10 = 3628800
        permutations. Now 1000000 lies somewhere between 362880*2 and 362880*3,
        therefore we know for certain that the first digit has to be the third one in
        the list, i.e., 2. Now, for the next digit, instead of looking for 1000000,
        we will look for 1000000 - (362880*2) and follow the same procedure using the
        8 remaining digits [0,1,3,4,5,6,7,8,9].
        """

        digits, limit = list(range(input_val[0])), input_val[1]
        result = []
        while len(digits) > 1:
            perm_count = factorial(len(digits) - 1)
            number_to_pop_idx = ceil(limit / perm_count)
            result.append(digits[number_to_pop_idx - 1])
            digits.remove(digits[number_to_pop_idx - 1])
            limit -= perm_count * (number_to_pop_idx - 1)
        result.append(digits[0])
        return int("".join(map(str, result)))

    def solver3(self, input_val):
        """ Same idea but a bit faster. """
        digits, limit = list(range(input_val[0])), input_val[1] - 1
        result = []

        for j in range(input_val[0] - 1, -1, -1):
            n = int(limit / factorial(j))
            result.append(str(digits[n]))
            limit -= n * factorial(j)
            del digits[n]

        return int("".join(result))


if __name__ == "__main__":
    unittest.main()
