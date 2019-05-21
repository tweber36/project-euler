from pyler import EulerProblem


class Problem0193(EulerProblem):
    """
    A positive integer n is called squarefree, if no square of a prime divides
    n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12. How
    many squarefree numbers are there below 250?
    """
    problem_id = 193
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

