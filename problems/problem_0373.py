from pyler import EulerProblem


class Problem0373(EulerProblem):
    """
    Every triangle has a circumscribed circle that goes through the three
    vertices. Consider all integer sided triangles for which the radius of the
    circumscribed circle is integral as well.   Let S(n) be the sum of the radii
    of the circumscribed circles of all such triangles for which the radius does
    not exceed n.  S(100)=4950 and S(1200)=1653605.   Find S(107).
    """
    problem_id = 373
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

