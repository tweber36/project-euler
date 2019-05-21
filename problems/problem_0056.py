from pyler import EulerProblem


class Problem0056(EulerProblem):
    """
    A googol (10100) is a massive number: one followed by one-hundred zeros;
    100100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.
    Considering natural numbers of the form, ab, where a, b < 100, what is the
    maximum digital sum?
    """
    problem_id = 56
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

