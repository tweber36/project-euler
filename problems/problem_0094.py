from pyler import EulerProblem


class Problem0094(EulerProblem):
    """
    It is easily proved that no equilateral triangle exists with integral length
    sides and integral area. However, the almost equilateral triangle 5-5-6 has
    an area of 12 square units. We shall define an almost equilateral triangle
    to be a triangle for which two sides are equal and the third differs by no
    more than one unit. Find the sum of the perimeters of all almost equilateral
    triangles with integral side lengths and area and whose perimeters do not
    exceed one billion (1,000,000,000).
    """
    problem_id = 94
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

