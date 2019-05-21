from pyler import EulerProblem


class Problem0041(EulerProblem):
    """
    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
    also prime. What is the largest n-digit pandigital prime that exists?
    """
    problem_id = 41
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

