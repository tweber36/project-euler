from pyler import EulerProblem


class Problem0551(EulerProblem):
    """
    Let a0, a1, a2, ... be an integer sequence defined by: a0 = 1; for n ≥ 1, an
    is the sum of the digits of all preceding terms. The sequence starts with 1,
    1, 2, 4, 8, 16, 23, 28, 38, 49, ... You are given a106 = 31054319. Find
    a1015.
    """
    problem_id = 551
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

