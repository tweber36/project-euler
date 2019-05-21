from pyler import EulerProblem


class Problem0032(EulerProblem):
    """
    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
    through 5 pandigital. The product 7254 is unusual, as the identity, 39 × 186
    = 7254, containing multiplicand, multiplier, and product is 1 through 9
    pandigital. Find the sum of all products whose
    multiplicand/multiplier/product identity can be written as a 1 through 9
    pandigital. HINT: Some products can be obtained in more than one way so be
    sure to only include it once in your sum.
    """
    problem_id = 32
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

