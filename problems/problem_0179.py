from pyler import EulerProblem


class Problem0179(EulerProblem):
    """
    Find the number of integers 1 < n < 107, for which n and n + 1 have the same
    number of positive divisors. For example, 14 has the positive divisors 1, 2,
    7, 14 while 15 has 1, 3, 5, 15.
    """
    problem_id = 179
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

