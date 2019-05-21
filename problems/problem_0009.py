from pyler import EulerProblem


class Problem0009(EulerProblem):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,  a2 + b2 = c2 For example, 32 + 42 = 9 + 16 = 25 = 52. There exists
    exactly one Pythagorean triplet for which a + b + c = 1000.Find the product
    abc.
    """
    problem_id = 9
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

