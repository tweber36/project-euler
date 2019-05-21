from pyler import EulerProblem


class Problem0164(EulerProblem):
    """
    How many 20 digit numbers n (without any leading zero) exist such that no
    three consecutive digits of n have a sum greater than 9?
    """
    problem_id = 164
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

