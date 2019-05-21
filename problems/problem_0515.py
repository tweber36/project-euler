from pyler import EulerProblem


class Problem0515(EulerProblem):
    """
    Let d(p,n,0) be the multiplicative inverse of n modulo prime p, defined as
    n × d(p,n,0) = 1 mod p. Let d(p,n,k) = $\sum_{i=1}^n$d(p,i,k−1) for k ≥ 1.
    Let D(a,b,k) = $\sum$(d(p,p-1,k) mod p) for all primes a ≤ p < a + b. You
    are given: D(101,1,10) = 45 D(103,102,102) = 8334 D(106,103,103) =
    38162302Find D(109,105,105).
    """
    problem_id = 515
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

