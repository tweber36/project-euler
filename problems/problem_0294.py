from pyler import EulerProblem


class Problem0294(EulerProblem):
    """
    For a positive integer k, define d(k) as the sum of the digits of k in its
    usual decimal representation. Thus d(42) = 4+2 = 6.   For a positive integer
    n, define S(n) as the number of positive integers k < 10n with the following
    properties : k is divisible by 23 and d(k) = 23.  You are given that S(9) =
    263626 and S(42) = 6377168878570056.   Find S(1112) and give your answer mod
    109.
    """
    problem_id = 294
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

