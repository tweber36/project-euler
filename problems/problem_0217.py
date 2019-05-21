from pyler import EulerProblem


class Problem0217(EulerProblem):
    """
    A positive integer with k (decimal) digits is called balanced if its first
    ⌈k/2⌉ digits sum to the same value as its last ⌈k/2⌉ digits, where ⌈x⌉,
    pronounced ceiling of x, is the smallest integer ≥ x, thus ⌈π⌉ = 4 and ⌈5⌉ =
    5. So, for example, all palindromes are balanced, as is 13722. Let T(n) be
    the sum of all balanced numbers less than 10n.  Thus: T(1) = 45, T(2) = 540
    and T(5) = 334795890.  Find T(47) mod 315
    """
    problem_id = 217
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

