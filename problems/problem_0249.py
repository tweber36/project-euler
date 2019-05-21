from pyler import EulerProblem


class Problem0249(EulerProblem):
    """
    Let S = {2, 3, 5, ..., 4999} be the set of prime numbers less than 5000.
    Find the number of subsets of S, the sum of whose elements is a prime
    number. Enter the rightmost 16 digits as your answer.
    """
    problem_id = 249
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

