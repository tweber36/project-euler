from pyler import EulerProblem


class Problem0529(EulerProblem):
    """
    A 10-substring of a number is a substring of its digits that sum to 10. For
    example, the 10-substrings of the number 3523014 are: 3523014 3523014
    3523014 3523014A number is called 10-substring-friendly if every one of its
    digits belongs to a 10-substring. For example, 3523014 is 10-substring-
    friendly, but 28546 is not. Let T(n) be the number of 10-substring-friendly
    numbers from 1 to 10n (inclusive). For example T(2) = 9 and T(5) = 3492.
    Find T(1018) mod 1 000 000 007.
    """
    problem_id = 529
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

