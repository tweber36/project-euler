from pyler import EulerProblem


class Problem0171(EulerProblem):
    """
    For a positive integer n, let f(n) be the sum of the squares of the digits
    (in base 10) of n, e.g. f(3) = 32 = 9, f(25) = 22 + 52 = 4 + 25 = 29, f(442)
    = 42 + 42 + 22 = 16 + 16 + 4 = 36 Find the last nine digits of the sum of
    all n, 0 < n < 1020, such that f(n) is a perfect square.
    """
    problem_id = 171
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

