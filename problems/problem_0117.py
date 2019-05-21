from pyler import EulerProblem


class Problem0117(EulerProblem):
    """
    Using a combination of grey square tiles and oblong tiles chosen from: red
    tiles (measuring two units), green tiles (measuring three units), and blue
    tiles (measuring four units), it is possible to tile a row measuring five
    units in length in exactly fifteen different ways.   How many ways can a row
    measuring fifty units in length be tiled? NOTE: This is related to Problem
    116.
    """
    problem_id = 117
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

