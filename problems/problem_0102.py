from pyler import EulerProblem


class Problem0102(EulerProblem):
    """
    Three distinct points are plotted at random on a Cartesian plane, for which
    -1000 ≤ x, y ≤ 1000, such that a triangle is formed. Consider the following
    two triangles: A(-340,495), B(-153,-910), C(835,-947) X(-175,41),
    Y(-421,-714), Z(574,-645) It can be verified that triangle ABC contains the
    origin, whereas triangle XYZ does not. Using triangles.txt (right click and
    'Save Link/Target As...'), a 27K text file containing the co-ordinates of
    one thousand "random" triangles, find the number of triangles for which the
    interior contains the origin. NOTE: The first two examples in the file
    represent the triangles in the example given above.
    """
    problem_id = 102
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

