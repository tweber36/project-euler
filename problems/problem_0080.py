from pyler import EulerProblem


class Problem0080(EulerProblem):
    """
    It is well known that if the square root of a natural number is not an
    integer, then it is irrational. The decimal expansion of such square roots
    is infinite without any repeating pattern at all. The square root of two is
    1.41421356237309504880..., and the digital sum of the first one hundred
    decimal digits is 475. For the first one hundred natural numbers, find the
    total of the digital sums of the first one hundred decimal digits for all
    the irrational square roots.
    """
    problem_id = 80
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

