import unittest
from pyler import EulerProblem
from math import factorial


class Problem0020(EulerProblem, unittest.TestCase):
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1 For example, 10! = 10 × 9 × ... × 3 ×
    2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8
    + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!
    """
    problem_id = 20
    simple_input = 10
    simple_output = 27
    real_input = 100
    real_output = 648
    
    def solver(self, input_val):
        return sum(map(int, str(factorial(input_val))))

if __name__ == '__main__':
    unittest.main()
