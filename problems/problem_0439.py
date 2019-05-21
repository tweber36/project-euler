from pyler import EulerProblem


class Problem0439(EulerProblem):
    """
    Let d(k) be the sum of all divisors of k. We define the function S(N) =
    $\sum_{i=1}^N \sum_{j=1}^Nd(i \cdot j)$. For example, S(3) = d(1) + d(2) +
    d(3) + d(2) + d(4) + d(6) + d(3) + d(6) + d(9) = 59. You are given that
    S(103) = 563576517282 and S(105) mod 109 = 215766508. Find S(1011) mod 109.
    """
    problem_id = 439
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

