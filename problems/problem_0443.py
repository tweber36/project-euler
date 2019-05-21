from pyler import EulerProblem


class Problem0443(EulerProblem):
    """
    Let g(n) be a sequence defined as follows: g(4) = 13, g(n) = g(n-1) + gcd(n,
    g(n-1)) for n > 4. The first few values are:
    n4567891011121314151617181920... g(n)1314161718272829303132333451545560...
    You are given that g(1 000) = 2524 and g(1 000 000) = 2624152. Find g(1015).
    """
    problem_id = 443
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

