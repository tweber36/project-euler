from pyler import EulerProblem


class Problem0178(EulerProblem):
    """
    Consider the number 45656.  It can be seen that each pair of consecutive
    digits of 45656 has a difference of one. A number for which every pair of
    consecutive digits has a difference of one is called a step number. A
    pandigital number  contains every decimal digit from 0 to 9 at least once.
    How many pandigital step numbers less than 1040 are there?
    """
    problem_id = 178
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

