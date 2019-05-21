from pyler import EulerProblem


class Problem0172(EulerProblem):
    """
    How many 18-digit numbers n (without leading zeros) are there such that no
    digit occurs more than three times in n?
    """
    problem_id = 172
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

