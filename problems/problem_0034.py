from pyler import EulerProblem


class Problem0034(EulerProblem):
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find the sum
    of all numbers which are equal to the sum of the factorial of their digits.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    problem_id = 34
    simple_input = 0
    simple_output = 1
    real_input = 0
    real_output = 1
    
    @staticmethod
    def solver(input_val):
        raise NotImplementedError


if __name__ == '__main__':
    import unittest
    unittest.main()

