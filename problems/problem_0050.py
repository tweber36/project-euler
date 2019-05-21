from pyler import EulerProblem


class Problem0050(EulerProblem):
    """
    The prime 41, can be written as the sum of six consecutive primes: 41 = 2 +
    3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes that adds
    to a prime below one-hundred. The longest sum of consecutive primes below
    one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
    """
    problem_id = 50
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

