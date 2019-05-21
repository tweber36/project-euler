from pyler import EulerProblem


class Problem0006(EulerProblem):
    """
    The sum of the squares of the first ten natural numbers is, 12 + 22 + ... +
    102 = 385 The square of the sum of the first ten natural numbers is, (1 + 2
    + ... + 10)2 = 552 = 3025 Hence the difference between the sum of the
    squares of the first ten natural numbers and the square of the sum is 3025 −
    385 = 2640. Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    """
    problem_id = 6
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

