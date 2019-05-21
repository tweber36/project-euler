from pyler import EulerProblem


class Problem0206(EulerProblem):
    """
    Find the unique positive integer whose square has the form
    1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.
    """
    problem_id = 206
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

