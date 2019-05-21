from pyler import EulerProblem


class Problem0047(EulerProblem):
    """
    The first two consecutive numbers to have two distinct prime factors are: 14
    = 2 × 715 = 3 × 5 The first three consecutive numbers to have three distinct
    prime factors are: 644 = 2² × 7 × 23645 = 3 × 5 × 43646 = 2 × 17 × 19. Find
    the first four consecutive integers to have four distinct prime factors
    each. What is the first of these numbers?
    """
    problem_id = 47
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

