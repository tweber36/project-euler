import unittest
from pyler import EulerProblem


class Problem0030(EulerProblem, unittest.TestCase):
    """
    Surprisingly there are only three numbers that can be written as the sum of
    fourth powers of their digits: 1634 = 14 + 64 + 34 + 44 8208 = 84 + 24 + 04
    + 84 9474 = 94 + 44 + 74 + 44 As 1 = 14 is not a sum it is not included. The
    sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the
    numbers that can be written as the sum of fifth powers of their digits.
    """

    problem_id = 30
    simple_input = 4
    simple_output = 19316
    real_input = 5
    real_output = 443839

    def find_n_digits_max(self, n):
        k = 1
        while 10 ** k <= (k + 1) * (9 ** n):
            k += 1
        return k

    def solver(self, input_val):
        n_digits_max = self.find_n_digits_max(input_val)
        result = 0
        for i in range(2, 10 ** n_digits_max):
            if i == sum(int(x) ** input_val for x in str(i)):
                result += i
        return result

    def solver2(self, input_val):
        """ https://projecteuler.net/thread=30;page=5#140138 """

        def genUniqueGroups(n_digits, lower=0, upper=9):
            # Recursive generator for unique groups of digits, length n_digits
            if n_digits == 1:
                for i in range(lower, upper + 1):
                    yield [i]
            else:
                for i in range(lower, upper + 1):
                    for j in genUniqueGroups(n_digits - 1, i, upper):
                        group = [i]
                        group.extend(j)
                        yield group

        n_digits_max = self.find_n_digits_max(input_val)
        # when all digits are over this value, stop looking
        limit = min([int(j) for j in str(n_digits_max * 9 ** input_val)])

        result = -1
        for digits_group in genUniqueGroups(n_digits_max):
            if digits_group[0] > limit:  # groups are sorted with lower value first
                break
            flag = True
            sum_pow_digits_group = sum([i ** input_val for i in digits_group])
            for j in map(int, str(sum_pow_digits_group)):
                if j in digits_group:
                    digits_group.remove(j)
                else:
                    flag = False
                    break
            if flag and sum(digits_group) == 0:  # all numbers accounted for
                result += sum_pow_digits_group
        return result


if __name__ == "__main__":
    unittest.main()
