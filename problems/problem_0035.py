from pyler import EulerProblem


class Problem0035(EulerProblem):
    """
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime. There are thirteen such
    primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How
    many circular primes are there below one million?
    """
    problem_id = 35
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

