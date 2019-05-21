from pyler import EulerProblem


class Problem0176(EulerProblem):
    """
    The four right-angled triangles with sides (9,12,15), (12,16,20), (5,12,13)
    and (12,35,37) all have one of the shorter sides (catheti) equal to 12. It
    can be shown that no other integer sided right-angled triangle exists with
    one of the catheti equal to 12. Find the smallest integer that can be the
    length of a cathetus of exactly 47547 different integer sided right-angled
    triangles.
    """
    problem_id = 176
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

