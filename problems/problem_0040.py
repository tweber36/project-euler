from pyler import EulerProblem


class Problem0040(EulerProblem):
    """
    An irrational decimal fraction is created by concatenating the positive
    integers: 0.123456789101112131415161718192021... It can be seen that the
    12th digit of the fractional part is 1. If dn represents the nth digit of
    the fractional part, find the value of the following expression. d1 × d10 ×
    d100 × d1000 × d10000 × d100000 × d1000000
    """
    problem_id = 40
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

