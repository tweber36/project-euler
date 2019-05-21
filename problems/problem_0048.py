from pyler import EulerProblem


class Problem0048(EulerProblem):
    """
    The series, 11 + 22 + 33 + ... + 1010 = 10405071317. Find the last ten
    digits of the series, 11 + 22 + 33 + ... + 10001000.
    """
    problem_id = 48
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

