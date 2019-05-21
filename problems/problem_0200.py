from pyler import EulerProblem


class Problem0200(EulerProblem):
    """
    We shall define a sqube to be a number of the form, p2q3, where p and q are
    distinct primes. For example, 200 = 5223 or 120072949 = 232613. The first
    five squbes are 72, 108, 200, 392, and 500. Interestingly, 200 is also the
    first number for which you cannot change any single digit to make a prime;
    we shall call such numbers, prime-proof. The next prime-proof sqube which
    contains the contiguous sub-string "200" is 1992008. Find the 200th prime-
    proof sqube containing the contiguous sub-string "200".
    """
    problem_id = 200
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

