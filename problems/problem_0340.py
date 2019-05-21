from pyler import EulerProblem


class Problem0340(EulerProblem):
    """
    For fixed integers a, b, c, define the crazy function F(n) as follows: F(n)
    = n - c for all n > b  F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.
    Also, define $S(a, b, c) = \sum \limits_{n = 0}^{b} {F(n)}$.  For example,
    if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040. Also,
    S(50, 2000, 40) = 5204240.   Find the last 9 digits of S(217, 721, 127).
    """
    problem_id = 340
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

