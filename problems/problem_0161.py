from pyler import EulerProblem


class Problem0161(EulerProblem):
    """
    A triomino is a shape consisting of three squares joined via the edges.
    There are two basic forms:  If all possible orientations are taken into
    account there are six:  Any n by m grid for which nxm is divisible by 3 can
    be tiled with triominoes. If we consider tilings that can be obtained by
    reflection or rotation from another tiling as different there are 41 ways a
    2 by 9 grid can be  tiled with triominoes:  In how many ways can a 9 by 12
    grid be tiled in this way by triominoes?
    """
    problem_id = 161
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

