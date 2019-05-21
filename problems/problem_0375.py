from pyler import EulerProblem


class Problem0375(EulerProblem):
    """
    Let Sn be an integer sequence produced with the following pseudo-random
    number generator: S0 =  290797  Sn+1 =  Sn2 mod 50515093   Let A(i, j) be
    the minimum of the numbers Si, Si+1, ... , Sj for i ≤ j. Let M(N) = ΣA(i, j)
    for 1 ≤ i ≤ j ≤ N. We can verify that M(10) = 432256955 and M(10 000) =
    3264567774119.  Find M(2 000 000 000).
    """
    problem_id = 375
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

