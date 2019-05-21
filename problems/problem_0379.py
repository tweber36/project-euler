from pyler import EulerProblem


class Problem0379(EulerProblem):
    """
    Let f(n) be the number of couples (x,y) with x and y positive integers, x ≤
    y and the least common multiple of x and y equal to n.   Let g be the
    summatory function of f, i.e.:  g(n) = ∑ f(i)  for 1 ≤ i ≤ n.   You are
    given that g(106) = 37429395.   Find g(1012).
    """
    problem_id = 379
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

