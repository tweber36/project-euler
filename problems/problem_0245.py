from pyler import EulerProblem


class Problem0245(EulerProblem):
    """
    We shall call a fraction that cannot be cancelled down a resilient fraction.
    Furthermore we shall define the resilience of a denominator, R(d), to be the
    ratio of its proper fractions that are resilient; for example, R(12) = 4⁄11.
    The resilience of a number d > 1 is then φ(d)d − 1 , where φ is Euler's
    totient function. We further define the coresilience of a number n > 1 as
    C(n)=  n − φ(n)n − 1. The coresilience of a prime p is C(p) =  1p − 1. Find
    the sum of all composite integers 1 < n ≤ 2×1011, for which C(n) is a unit
    fraction.
    """
    problem_id = 245
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

