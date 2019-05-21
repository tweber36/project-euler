from pyler import EulerProblem


class Problem0398(EulerProblem):
    """
    Inside a rope of length n, n-1 points are placed with distance 1 from each
    other and from the endpoints. Among these points, we choose m-1 points at
    random and cut the rope at these points to create m segments.   Let E(n, m)
    be the expected length of the second-shortest segment. For example, E(3, 2)
    = 2 and E(8, 3) = 16/7. Note that if multiple segments have the same
    shortest length the length of the second-shortest segment is defined as the
    same as the shortest length.   Find E(107, 100). Give your answer rounded to
    5 decimal places behind the decimal point.
    """
    problem_id = 398
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

