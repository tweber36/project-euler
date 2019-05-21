from pyler import EulerProblem


class Problem0168(EulerProblem):
    """
    Consider the number 142857. We can right-rotate this number by moving the
    last digit (7) to the front of it, giving us 714285. It can be verified that
    714285=5×142857. This demonstrates an unusual property of 142857: it is a
    divisor of its right-rotation. Find the last 5 digits of the sum of all
    integers n, 10 < n < 10100, that have this property.
    """
    problem_id = 168
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

