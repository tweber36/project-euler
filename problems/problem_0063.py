from pyler import EulerProblem


class Problem0063(EulerProblem):
    """
    The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
    number, 134217728=89, is a ninth power. How many n-digit positive integers
    exist which are also an nth power?
    """
    problem_id = 63
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

