from pyler import EulerProblem


class Problem0142(EulerProblem):
    """
    Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x −
    y, x + z, x − z, y + z, y − z are all perfect squares.
    """
    problem_id = 142
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

