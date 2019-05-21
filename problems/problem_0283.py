from pyler import EulerProblem


class Problem0283(EulerProblem):
    """
    Consider the triangle with sides 6, 8 and 10. It can be seen that the
    perimeter and the area are both equal to 24.  So the area/perimeter ratio is
    equal to 1. Consider also the triangle with sides 13, 14 and 15. The
    perimeter equals 42 while the area is equal to 84.  So for this triangle the
    area/perimeter ratio is equal to 2.   Find the sum of the perimeters of all
    integer sided triangles for which the area/perimeter ratios are equal to
    positive integers not exceeding 1000.
    """
    problem_id = 283
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

