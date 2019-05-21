from pyler import EulerProblem


class Problem0317(EulerProblem):
    """
    A firecracker explodes at a height of 100 m above level ground. It breaks
    into a large number of very small fragments, which move in every direction;
    all of them have the same initial velocity of 20 m/s.   We assume that the
    fragments move without air resistance, in a uniform gravitational field with
    g=9.81 m/s2.   Find the volume (in m3) of the region through which the
    fragments move before reaching the ground.  Give your answer rounded to four
    decimal places.
    """
    problem_id = 317
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

