from pyler import EulerProblem


class Problem0138(EulerProblem):
    """
    Consider the isosceles triangle with base length, b = 16, and legs, L = 17.
    By using the Pythagorean theorem it can be seen that the height of the
    triangle, h = √(172 − 82) = 15, which is one less than the base length. With
    b = 272 and L = 305, we get h = 273, which is one more than the base length,
    and this is the second smallest isosceles triangle with the property that h
    = b ± 1. Find ∑ L for the twelve smallest isosceles triangles for which h =
    b ± 1 and b, L are positive integers.
    """
    problem_id = 138
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

