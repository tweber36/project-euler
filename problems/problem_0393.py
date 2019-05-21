from pyler import EulerProblem


class Problem0393(EulerProblem):
    """
    An  n×n grid of squares contains  n2 ants, one ant per square. All ants
    decide to move simultaneously to an adjacent square (usually 4
    possibilities, except for ants on the edge of the grid or at the corners).
    We define f(n) to be the number of ways this can happen without any ants
    ending on the same square and without any two ants crossing the same edge
    between two squares.   You are given that f(4) = 88. Find  f(10).
    """
    problem_id = 393
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

