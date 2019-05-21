from pyler import EulerProblem


class Problem0030(EulerProblem):
    """
    Surprisingly there are only three numbers that can be written as the sum of
    fourth powers of their digits: 1634 = 14 + 64 + 34 + 44 8208 = 84 + 24 + 04
    + 84 9474 = 94 + 44 + 74 + 44 As 1 = 14 is not a sum it is not included. The
    sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the
    numbers that can be written as the sum of fifth powers of their digits.
    """
    problem_id = 30
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

