from pyler import EulerProblem


class Problem0077(EulerProblem):
    """
    It is possible to write ten as the sum of primes in exactly five different
    ways: 7 + 3 5 + 5 5 + 3 + 2 3 + 3 + 2 + 2 2 + 2 + 2 + 2 + 2 What is the
    first value which can be written as the sum of primes in over five thousand
    different ways?
    """
    problem_id = 77
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

