from pyler import EulerProblem


class Problem0266(EulerProblem):
    """
    The divisors of 12 are: 1,2,3,4,6 and 12. The largest divisor of 12 that
    does not exceed the square root of 12 is 3. We shall call the largest
    divisor of an integer n that does not exceed the square root of n the pseudo
    square root (PSR) of n. It can be seen that PSR(3102)=47.   Let p be the
    product of the primes below 190. Find PSR(p) mod 1016.
    """
    problem_id = 266
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

