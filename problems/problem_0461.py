from pyler import EulerProblem


class Problem0461(EulerProblem):
    """
    Let fn(k) = ek/n - 1, for all non-negative integers k. Remarkably,
    f200(6) + f200(75) + f200(89) + f200(226) = 3.141592644529… ≈ π. In fact, it
    is the best approximation of π of the form fn(a) + fn(b) + fn(c) + fn(d) for
    n = 200. Let g(n) = a2 + b2 + c2 + d 2 for a, b, c, d that minimize the
    error: | fn(a) + fn(b) + fn(c) + fn(d) - π| (where |x| denotes the absolute
    value of x). You are given g(200) = 62 + 752 + 892 + 2262 = 64658. Find
    g(10000).
    """
    problem_id = 461
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

