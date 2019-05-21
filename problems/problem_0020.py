from pyler import EulerProblem


class Problem0020(EulerProblem):
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1 For example, 10! = 10 × 9 × ... × 3 ×
    2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8
    + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!
    """
    problem_id = 20
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

