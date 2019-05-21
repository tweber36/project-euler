from pyler import EulerProblem


class Problem0085(EulerProblem):
    """
    By counting carefully it can be seen that a rectangular grid measuring 3 by
    2 contains eighteen rectangles:   Although there exists no rectangular grid
    that contains exactly two million rectangles, find the area of the grid with
    the nearest solution.
    """
    problem_id = 85
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

