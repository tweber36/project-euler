from pyler import EulerProblem


class Problem0231(EulerProblem):
    """
    The binomial coefficient 10C3 = 120. 120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5,
    and 2 + 2 + 2 + 3 + 5 = 14. So the sum of the terms in the prime
    factorisation of 10C3 is 14.  Find the sum of the terms in the prime
    factorisation of 20000000C15000000.
    """
    problem_id = 231
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

