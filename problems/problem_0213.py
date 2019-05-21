from pyler import EulerProblem


class Problem0213(EulerProblem):
    """
    A 30×30 grid of squares contains 900 fleas, initially one flea per square.
    When a bell is rung, each flea jumps to an adjacent square at random
    (usually 4 possibilities, except for fleas on the edge of the grid or at the
    corners). What is the expected number of unoccupied squares after 50 rings
    of the bell? Give your answer rounded to six decimal places.
    """
    problem_id = 213
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

