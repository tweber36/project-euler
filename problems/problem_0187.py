from pyler import EulerProblem


class Problem0187(EulerProblem):
    """
    A composite is a number containing at least two prime factors. For example,
    15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3. There are ten composites below thirty
    containing precisely two, not necessarily distinct, prime factors: 4, 6, 9,
    10, 14, 15, 21, 22, 25, 26. How many composite integers, n < 108, have
    precisely two, not necessarily distinct, prime factors?
    """
    problem_id = 187
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

