from pyler import EulerProblem


class Problem0016(EulerProblem):
    """
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is the
    sum of the digits of the number 21000?
    """
    problem_id = 16
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

