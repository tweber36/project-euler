from pyler import EulerProblem


class Problem0549(EulerProblem):
    """
    The smallest number m such that 10 divides m! is m=5. The smallest number m
    such that 25 divides m! is m=10.  Let s(n) be the smallest number m such
    that n divides m!. So s(10)=5 and s(25)=10. Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
    S(100)=2012.   Find S(108).
    """
    problem_id = 549
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

