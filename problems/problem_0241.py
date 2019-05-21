from pyler import EulerProblem


class Problem0241(EulerProblem):
    """
    For a positive integer n, let σ(n) be the sum of all divisors of n, so e.g.
    σ(6) = 1 + 2 + 3 + 6 = 12.  A perfect number, as you probably know, is a
    number with σ(n) = 2n. Let us define the perfection quotient of a positive
    integer asp(n)=  σ(n)n . Find the sum of all positive integers n ≤ 1018 for
    which p(n) has the form k + 1⁄2, where k is an integer.
    """
    problem_id = 241
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

