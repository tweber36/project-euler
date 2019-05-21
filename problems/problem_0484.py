from pyler import EulerProblem


class Problem0484(EulerProblem):
    """
    The arithmetic derivative is defined by p' = 1 for any prime p (ab)' = a'b +
    ab' for all integers a, b (Leibniz rule) For example, 20' = 24 Find ∑
    gcd(k,k') for 1 < k ≤ 5·1015 Note: gcd(x,y) denotes the greatest common
    divisor of x and y.
    """
    problem_id = 484
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

