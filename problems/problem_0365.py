from pyler import EulerProblem


class Problem0365(EulerProblem):
    """
    The binomial coefficient C(1018,109) is a number with more than 9 billion
    (9×109) digits.   Let M(n,k,m) denote the binomial coefficient C(n,k) modulo
    m.   Calculate ∑M(1018,109,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.
    """
    problem_id = 365
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

