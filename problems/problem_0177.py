from pyler import EulerProblem


class Problem0177(EulerProblem):
    """
    Let ABCD be a convex quadrilateral, with diagonals AC and BD. At each vertex
    the diagonal makes an angle with each of the two sides, creating eight
    corner angles.  For example, at vertex A, the two angles are CAD, CAB. We
    call such a quadrilateral for which all eight corner angles have integer
    values when measured in degrees an "integer angled quadrilateral". An
    example of an integer angled quadrilateral is a square, where all eight
    corner angles are 45°. Another example is given by DAC = 20°, BAC = 60°, ABD
    = 50°, CBD = 30°, BCA = 40°, DCA = 30°, CDB = 80°, ADB = 50°. What is the
    total number of non-similar integer angled quadrilaterals? Note: In your
    calculations you may assume that a calculated angle is integral if it is
    within a tolerance of 10-9 of an integer value.
    """
    problem_id = 177
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

