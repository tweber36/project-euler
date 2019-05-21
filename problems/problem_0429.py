from pyler import EulerProblem


class Problem0429(EulerProblem):
    """
    A unitary divisor d of a number n is a divisor of n that has the property
    gcd(d, n/d) = 1. The unitary divisors of 4! = 24 are 1, 3, 8 and 24. The sum
    of their squares is 12 + 32 + 82 + 242 = 650.   Let S(n) represent the sum
    of the squares of the unitary divisors of n. Thus S(4!)=650.   Find S(100
    000 000!) modulo 1 000 000 009.
    """
    problem_id = 429
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

