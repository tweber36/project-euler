from pyler import EulerProblem


class Problem0116(EulerProblem):
    """
    A row of five grey square tiles is to have a number of its tiles replaced
    with coloured oblong tiles chosen from red (length two), green (length
    three), or blue (length four). If red tiles are chosen there are exactly
    seven ways this can be done.   If green tiles are chosen there are three
    ways.   And if blue tiles are chosen there are two ways.   Assuming that
    colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey
    tiles in a row measuring five units in length. How many different ways can
    the grey tiles in a row measuring fifty units in length be replaced if
    colours cannot be mixed and at least one coloured tile must be used? NOTE:
    This is related to Problem 117.
    """
    problem_id = 116
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

