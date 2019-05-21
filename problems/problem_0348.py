from pyler import EulerProblem


class Problem0348(EulerProblem):
    """
    Many numbers can be expressed as the sum of a square and a cube. Some of
    them in more than one way. Consider the palindromic numbers that can be
    expressed as the sum of a square and a cube, both greater than 1, in exactly
    4 different ways. For example, 5229225 is a palindromic number and it can be
    expressed in exactly 4 different ways: 22852 + 203 22232 + 663 18102 + 1253
    11972 + 1563 Find the sum of the five smallest such palindromic numbers.
    """
    problem_id = 348
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

