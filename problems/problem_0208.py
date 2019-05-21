from pyler import EulerProblem


class Problem0208(EulerProblem):
    """
    A robot moves in a series of one-fifth circular arcs (72°), with a free
    choice of a clockwise or an anticlockwise arc for each step, but no turning
    on the spot. One of 70932 possible closed paths of 25 arcs starting
    northward is   Given that the robot starts facing North, how many journeys
    of 70 arcs in length can it take that return it, after the final arc, to its
    starting position? (Any arc may be traversed multiple times.)
    """
    problem_id = 208
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

