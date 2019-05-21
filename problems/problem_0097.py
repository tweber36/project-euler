from pyler import EulerProblem


class Problem0097(EulerProblem):
    """
    The first known prime found to exceed one million digits was discovered in
    1999, and is a Mersenne prime of the form 26972593−1; it contains exactly
    2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have
    been found which contain more digits. However, in 2004 there was found a
    massive non-Mersenne prime which contains 2,357,207 digits:
    28433×27830457+1. Find the last ten digits of this prime number.
    """
    problem_id = 97
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

