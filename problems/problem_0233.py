from pyler import EulerProblem


class Problem0233(EulerProblem):
    """
    Let f(N) be the number of points with integer coordinates that are on a
    circle passing through (0,0), (N,0),(0,N), and (N,N). It can be shown that
    f(10000) = 36. What is the sum of all positive integers N ≤ 1011 such that
    f(N) = 420 ?
    """
    problem_id = 233
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

