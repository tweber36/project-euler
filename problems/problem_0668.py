from pyler import EulerProblem


class Problem0668(EulerProblem):
    """
    A positive integer is called square root smooth if all of its prime factors
    are strictly less than its square root. Including the number $1$, there are
    $29$ square root smooth numbers not exceeding $100$.   How many square root
    smooth numbers are there not exceeding $10\,000\,000\,000$?
    """
    problem_id = 668
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

