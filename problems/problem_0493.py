from pyler import EulerProblem


class Problem0493(EulerProblem):
    """
    70 coloured balls are placed in an urn, 10 for each of the seven rainbow
    colours. What is the expected number of distinct colours in 20 randomly
    picked balls? Give your answer with nine digits after the decimal point
    (a.bcdefghij).
    """
    problem_id = 493
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

