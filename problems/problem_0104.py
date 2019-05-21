from pyler import EulerProblem


class Problem0104(EulerProblem):
    """
    The Fibonacci sequence is defined by the recurrence relation: Fn = Fn−1 +
    Fn−2, where F1 = 1 and F2 = 1. It turns out that F541, which contains 113
    digits, is the first Fibonacci number for which the last nine digits are 1-9
    pandigital (contain all the digits 1 to 9, but not necessarily in order).
    And F2749, which contains 575 digits, is the first Fibonacci number for
    which the first nine digits are 1-9 pandigital. Given that Fk is the first
    Fibonacci number for which the first nine digits AND the last nine digits
    are 1-9 pandigital, find k.
    """
    problem_id = 104
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

