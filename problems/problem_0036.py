from pyler import EulerProblem


class Problem0036(EulerProblem):
    """
    The decimal number, 585 = 10010010012 (binary), is palindromic in both
    bases. Find the sum of all numbers, less than one million, which are
    palindromic in base 10 and base 2. (Please note that the palindromic number,
    in either base, may not include leading zeros.)
    """
    problem_id = 36
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

