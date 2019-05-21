from pyler import EulerProblem


class Problem0033(EulerProblem):
    """
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
    is correct, is obtained by cancelling the 9s. We shall consider fractions
    like, 30/50 = 3/5, to be trivial examples. There are exactly four non-
    trivial examples of this type of fraction, less than one in value, and
    containing two digits in the numerator and denominator. If the product of
    these four fractions is given in its lowest common terms, find the value of
    the denominator.
    """
    problem_id = 33
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

