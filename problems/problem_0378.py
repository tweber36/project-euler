from pyler import EulerProblem


class Problem0378(EulerProblem):
    """
    Let T(n) be the nth triangle number, so T(n) =   n (n+1)2  .   Let dT(n) be
    the number of divisors of T(n). E.g.: T(7) = 28 and dT(7) = 6.   Let Tr(n)
    be the number of triples (i, j, k) such that 1 ≤ i < j < k ≤ n and dT(i) >
    dT(j) > dT(k). Tr(20) = 14, Tr(100) = 5772 and Tr(1000) = 11174776.   Find
    Tr(60 000 000).  Give the last 18 digits of your answer.
    """
    problem_id = 378
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

