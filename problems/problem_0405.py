from pyler import EulerProblem


class Problem0405(EulerProblem):
    """
    We wish to tile a rectangle whose length is twice its width. Let T(0) be the
    tiling consisting of a single rectangle. For n > 0, let T(n) be obtained
    from T(n-1) by replacing all tiles in the following manner:     The
    following animation demonstrates the tilings T(n) for n from 0 to 5:     Let
    f(n) be the number of points where four tiles meet in T(n). For example,
    f(1) = 0, f(4) = 82 and f(109) mod 177 = 126897180.   Find f(10k) for k =
    1018, give your answer modulo 177.
    """
    problem_id = 405
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

