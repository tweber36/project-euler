from pyler import EulerProblem


class Problem0135(EulerProblem):
    """
    Given the positive integers, x, y, and z, are consecutive terms of an
    arithmetic progression, the least value of the positive integer, n, for
    which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:
    342 − 272 − 202 = 122 − 92 − 62 = 27 It turns out that n = 1155 is the least
    value which has exactly ten solutions. How many values of n less than one
    million have exactly ten distinct solutions?
    """
    problem_id = 135
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

