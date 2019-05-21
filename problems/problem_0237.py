from pyler import EulerProblem


class Problem0237(EulerProblem):
    """
    Let T(n) be the number of tours over a 4 × n playing board such that: The
    tour starts in the top left corner. The tour consists of moves that are up,
    down, left, or right one square. The tour visits each square exactly once.
    The tour ends in the bottom left corner. The diagram shows one tour over a 4
    × 10 board:   T(10) is 2329. What is T(1012) modulo 108?
    """
    problem_id = 237
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

