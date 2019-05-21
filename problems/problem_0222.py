from pyler import EulerProblem


class Problem0222(EulerProblem):
    """
    What is the length of the shortest pipe, of internal radius 50mm, that can
    fully contain 21 balls of radii 30mm, 31mm, ..., 50mm? Give your answer in
    micrometres (10-6 m) rounded to the nearest integer.
    """
    problem_id = 222
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

