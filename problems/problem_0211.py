from pyler import EulerProblem


class Problem0211(EulerProblem):
    """
    For a positive integer n, let σ2(n) be the sum of the squares of its
    divisors. For example, σ2(10) = 1 + 4 + 25 + 100 = 130. Find the sum of all
    n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.
    """
    problem_id = 211
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

