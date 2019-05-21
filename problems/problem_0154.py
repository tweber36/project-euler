from pyler import EulerProblem


class Problem0154(EulerProblem):
    """
    A triangular pyramid is constructed using spherical balls so that each ball
    rests on exactly three balls of the next lower level.  Then, we calculate
    the number of paths leading from the apex to each position: A path starts at
    the apex and progresses downwards to any of the three spheres directly below
    the current position. Consequently, the number of paths to reach a certain
    position is the sum of the numbers immediately above it (depending on the
    position, there are up to three numbers above it). The result is Pascal's
    pyramid and the numbers at each level n are the coefficients of the
    trinomial expansion  (x + y + z)n. How many coefficients in the expansion of
    (x + y + z)200000 are multiples of 1012?
    """
    problem_id = 154
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

