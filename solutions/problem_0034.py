from math import factorial

from pyler.pyler import EulerProblem


class Problem0034(EulerProblem):
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find the sum
    of all numbers which are equal to the sum of the factorial of their digits.
    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
    """
    problem_id = 34
    simple_input = 0
    simple_output = 40730
    real_input = 0
    real_output = 40730

    @staticmethod
    def solver(input_val):
        def upper_bound():
            n_digits = 1
            fact_9 = factorial(9)
            while n_digits * fact_9 >= 10 ** n_digits:
                n_digits += 1
            return 10 ** n_digits

        factorials = {str(x): factorial(x) for x in range(10)}
        result = 0
        for i in range(10, upper_bound()):
            digits_factorials = [factorials[x] for x in str(i)]
            if sum(digits_factorials) == i:
                result += i
        return result


if __name__ == '__main__':
    import unittest
    unittest.main()
