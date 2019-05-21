from pyler import EulerProblem


class Problem0381(EulerProblem):
    """
    For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.   For example, if
    p=7, (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! =
    720+120+24+6+2 = 872.  As 872 mod(7) = 4, S(7) = 4.   It can be verified
    that ∑S(p) = 480 for 5 ≤ p < 100.   Find ∑S(p) for 5 ≤ p < 108.
    """
    problem_id = 381
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

