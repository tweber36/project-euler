from pyler import EulerProblem


class Problem0076(EulerProblem):
    """
    It is possible to write five as a sum in exactly six different ways: 4 + 1 3
    + 2 3 + 1 + 1 2 + 2 + 1 2 + 1 + 1 + 1 1 + 1 + 1 + 1 + 1 How many different
    ways can one hundred be written as a sum of at least two positive integers?
    """
    problem_id = 76
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

