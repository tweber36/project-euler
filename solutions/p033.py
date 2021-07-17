from fractions import Fraction

from pyler.pyler import EulerProblem


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

    https://projecteuler.net/action=quote;post_id=5553
    https://projecteuler.net/action=quote;post_id=86864
    https://projecteuler.net/action=quote;post_id=102390
    """
    problem_id = 33
    simple_input = 0
    simple_output = 100
    real_input = 0
    real_output = 100

    @staticmethod
    def solver(input_val):
        product_numerator, product_denominator = 1, 1
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(b + 1, 10):
                    for n, d in (10 * a + b, 10 * c + a), (10 * b + a, 10 * a + c):
                        if n < d and n * c == b * d:
                            product_numerator, product_denominator = product_numerator * n, product_denominator * d
        return Fraction(product_numerator, product_denominator).denominator


if __name__ == '__main__':
    import unittest
    unittest.main()

