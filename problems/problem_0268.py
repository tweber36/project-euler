from pyler import EulerProblem


class Problem0268(EulerProblem):
    """
    It can be verified that there are 23 positive integers less than 1000 that
    are divisible by at least four distinct primes less than 100. Find how many
    positive integers less than 1016 are divisible by at least four distinct
    primes less than 100.
    """
    problem_id = 268
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

