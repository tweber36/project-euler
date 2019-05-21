from pyler import EulerProblem


class Problem0322(EulerProblem):
    """
    Let T(m, n) be the number of the binomial coefficients iCn that are
    divisible by 10 for n ≤ i < m(i, m and n are positive integers). You are
    given that T(109, 107-10) = 989697000.   Find T(1018, 1012-10).
    """
    problem_id = 322
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

