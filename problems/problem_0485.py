from pyler import EulerProblem


class Problem0485(EulerProblem):
    """
    Let d(n) be the number of divisors of n. Let M(n,k) be the maximum value of
    d(j) for n ≤ j ≤ n+k-1. Let S(u,k) be the sum of M(n,k) for 1 ≤ n ≤ u-k+1.
    You are given that S(1000,10)=17176.   Find S(100 000 000,100 000).
    """
    problem_id = 485
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

