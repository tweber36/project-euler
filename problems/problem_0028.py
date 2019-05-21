from pyler import EulerProblem


class Problem0028(EulerProblem):
    """
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows: 21 22 23 24 25 20  7  8  9 10 19  6  1
     2 11 18  5  4  3 1217 16 15 14 13 It can be verified that the sum of the
    numbers on the diagonals is 101. What is the sum of the numbers on the
    diagonals in a 1001 by 1001 spiral formed in the same way?
    """
    problem_id = 28
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

