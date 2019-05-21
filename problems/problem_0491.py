from pyler import EulerProblem


class Problem0491(EulerProblem):
    """
    We call a positive integer double pandigital if it uses all the digits 0 to
    9 exactly twice (with no leading zero). For example, 40561817703823564929 is
    one such number. How many double pandigital numbers are divisible by 11?
    """
    problem_id = 491
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

