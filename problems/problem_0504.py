from pyler import EulerProblem


class Problem0504(EulerProblem):
    """
    Let ABCD be a quadrilateral whose vertices are lattice points lying on the
    coordinate axes as follows: A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤
    a, b, c, d ≤ m and a, b, c, d, m are integers. It can be shown that for m =
    4 there are exactly 256 valid ways to construct ABCD. Of these 256
    quadrilaterals, 42 of them strictly contain a square number of lattice
    points. How many quadrilaterals ABCD strictly contain a square number of
    lattice points for m = 100?
    """
    problem_id = 504
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

