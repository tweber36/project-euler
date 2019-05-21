from pyler import EulerProblem


class Problem0290(EulerProblem):
    """
    How many integers 0 ≤ n < 1018 have the property that the sum of the digits
    of n equals the sum of digits of 137n?
    """
    problem_id = 290
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

