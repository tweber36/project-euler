from pyler import EulerProblem


class Problem0457(EulerProblem):
    """
    Let f(n) = n2 - 3n - 1. Let p be a prime. Let R(p) be the smallest positive
    integer n such that f(n) mod p2 = 0 if such an integer n exists, otherwise
    R(p) = 0.   Let SR(L) be ∑R(p) for all primes not exceeding L.   Find
    SR(107).
    """
    problem_id = 457
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

