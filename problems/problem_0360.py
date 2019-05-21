from pyler import EulerProblem


class Problem0360(EulerProblem):
    """
    Given two points (x1,y1,z1) and (x2,y2,z2) in three dimensional space, the
    Manhattan distance  between those points is defined as
    |x1-x2|+|y1-y2|+|z1-z2|.   Let C(r) be a sphere with radius r and center in
    the origin O(0,0,0). Let I(r) be the set of all points with integer
    coordinates on the surface of C(r). Let S(r) be the sum of the Manhattan
    distances of all elements of I(r) to the origin O.   E.g. S(45)=34518.
    Find S(1010).
    """
    problem_id = 360
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

