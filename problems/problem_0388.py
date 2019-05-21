from pyler import EulerProblem


class Problem0388(EulerProblem):
    """
    Consider all lattice points (a,b,c) with 0 ≤ a,b,c ≤ N.   From the origin
    O(0,0,0) all lines are drawn to the other lattice points. Let D(N) be the
    number of distinct such lines.   You are given that D(1 000 000) =
    831909254469114121.  Find D(1010). Give as your answer the first nine digits
    followed by the last nine digits.
    """
    problem_id = 388
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

