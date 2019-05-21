from pyler import EulerProblem


class Problem0421(EulerProblem):
    """
    Numbers of the form n15+1 are composite for every integer n > 1. For
    positive integers n and m let s(n,m) be defined as the sum of the distinct
    prime factors of n15+1 not exceeding m.  E.g. 215+1 = 3×3×11×331. So s(2,10)
    = 3 and s(2,1000) = 3+11+331 = 345.  Also 1015+1 =
    7×11×13×211×241×2161×9091. So s(10,100) = 31 and s(10,1000) = 483. Find ∑
    s(n,108) for 1 ≤ n ≤ 1011.
    """
    problem_id = 421
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

