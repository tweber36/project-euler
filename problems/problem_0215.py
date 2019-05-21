from pyler import EulerProblem


class Problem0215(EulerProblem):
    """
    Consider the problem of building a wall out of 2×1 and 3×1 bricks
    (horizontal×vertical dimensions) such that, for extra strength, the gaps
    between horizontally-adjacent bricks never line up in consecutive layers,
    i.e. never form a "running crack". For example, the following 9×3 wall is
    not acceptable due to the running crack shown in red:   There are eight ways
    of forming a crack-free 9×3 wall, written W(9,3) = 8. Calculate W(32,10).
    """
    problem_id = 215
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

