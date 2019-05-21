from pyler import EulerProblem


class Problem0389(EulerProblem):
    """
    An unbiased single 4-sided die is thrown and its value, T, is noted.T
    unbiased 6-sided dice are thrown and their scores are added together. The
    sum, C, is noted.C unbiased 8-sided dice are thrown and their scores are
    added together. The sum, O, is noted.O unbiased 12-sided dice are thrown and
    their scores are added together. The sum, D, is noted.D unbiased 20-sided
    dice are thrown and their scores are added together. The sum, I, is noted.
    Find the variance of I, and give your answer rounded to 4 decimal places.
    """
    problem_id = 389
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

