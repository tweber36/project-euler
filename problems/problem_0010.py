from pyler import EulerProblem


class Problem0010(EulerProblem):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
    the primes below two million.
    """
    problem_id = 10
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

