from pyler import EulerProblem


class Problem0248(EulerProblem):
    """
    The first number n for which φ(n)=13! is 6227180929. Find the 150,000th such
    number.
    """
    problem_id = 248
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

