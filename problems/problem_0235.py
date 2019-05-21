from pyler import EulerProblem


class Problem0235(EulerProblem):
    """
    Given is the arithmetic-geometric sequence u(k) = (900-3k)rk-1. Let s(n) =
    Σk=1...nu(k).   Find the value of r for which s(5000) = -600,000,000,000.
    Give your answer rounded to 12 places behind the decimal point.
    """
    problem_id = 235
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

