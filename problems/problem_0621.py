from pyler import EulerProblem


class Problem0621(EulerProblem):
    """
    Gauss famously proved that every positive integer can be expressed as the
    sum of three triangular numbers (including 0 as the lowest triangular
    number).  In fact most numbers can be expressed as a sum of three triangular
    numbers in several ways.  Let $G(n)$ be the number of ways of expressing $n$
    as the sum of three triangular numbers, regarding different arrangements of
    the terms of the sum as distinct.  For example, $G(9) = 7$, as 9 can be
    expressed as:  3+3+3, 0+3+6, 0+6+3, 3+0+6, 3+6+0, 6+0+3, 6+3+0.   You are
    given $G(1000) = 78$ and $G(10^6) = 2106$.  Find $G(17 526 \times 10^9)$.
    """
    problem_id = 621
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

