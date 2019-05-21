from pyler import EulerProblem


class Problem0052(EulerProblem):
    """
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order. Find the smallest
    positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same
    digits.
    """
    problem_id = 52
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

