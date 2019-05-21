from pyler import EulerProblem


class Problem0596(EulerProblem):
    """
    Let T(r) be the number of integer quadruplets x, y, z, t such that x2 + y2 +
    z2 + t2 ≤ r2. In other words, T(r) is the number of lattice points in the
    four-dimensional hyperball of radius r. You are given that T(2) = 89, T(5) =
    3121, T(100) = 493490641 and T(104) = 49348022079085897. Find T(108) mod
    1000000007.
    """
    problem_id = 596
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

