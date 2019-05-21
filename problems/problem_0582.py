from pyler import EulerProblem


class Problem0582(EulerProblem):
    """
    Let a, b and c be the sides of an integer sided triangle with one angle of
    120 degrees, a≤b≤c and b-a≤100. Let T(n) be the number of such triangles
    with c≤n. T(1000)=235 and T(108)=1245. Find T(10100).
    """
    problem_id = 582
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

