from pyler import EulerProblem


class Problem0250(EulerProblem):
    """
    Find the number of non-empty subsets of {11, 22, 33,..., 250250250250}, the
    sum of whose elements is divisible by 250. Enter the rightmost 16 digits as
    your answer.
    """
    problem_id = 250
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

