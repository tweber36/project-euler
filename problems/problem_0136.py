from pyler import EulerProblem


class Problem0136(EulerProblem):
    """
    The positive integers, x, y, and z, are consecutive terms of an arithmetic
    progression. Given that n is a positive integer, the equation, x2 − y2 − z2
    = n, has exactly one solution when n = 20: 132 − 102 − 72 = 20 In fact there
    are twenty-five values of n below one hundred for which the equation has a
    unique solution. How many values of n less than fifty million have exactly
    one solution?
    """
    problem_id = 136
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

