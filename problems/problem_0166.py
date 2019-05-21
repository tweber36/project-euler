from pyler import EulerProblem


class Problem0166(EulerProblem):
    """
    A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9. It can be seen that in the
    grid  6 3 3 0 5 0 4 3 0 7 1 4 1 2 4 5 the sum of each row and each column
    has the value 12. Moreover the sum of each diagonal is also 12. In how many
    ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row,
    each column, and both diagonals have the same sum?
    """
    problem_id = 166
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

