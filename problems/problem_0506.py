from pyler import EulerProblem


class Problem0506(EulerProblem):
    """
    Consider the infinite repeating sequence of digits: 1234321234321234321...
    Amazingly, you can break this sequence of digits into a sequence of integers
    such that the sum of the digits in the n'th value is n. The sequence goes as
    follows: 1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ... Let vn be the
    n'th value in this sequence. For example, v2 = 2, v5 = 32 and v11 = 32123.
    Let S(n) be v1 + v2 + ... + vn. For example, S(11) = 36120, and
    S(1000) mod 123454321 = 18232686. Find S(1014) mod 123454321.
    """
    problem_id = 506
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

