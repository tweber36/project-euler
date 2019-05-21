from pyler import EulerProblem


class Problem0455(EulerProblem):
    """
    Let f(n) be the largest positive integer x less than 109 such that the last
    9 digits of nx form the number x (including leading zeros), or zero if no
    such integer exists. For example: f(4) = 411728896 (4411728896 =
    ...490411728896)  f(10) = 0 f(157) = 743757 (157743757 = ...567000743757)
    Σf(n), 2 ≤ n ≤ 103 = 442530011399 Find Σf(n), 2 ≤ n ≤ 106.
    """
    problem_id = 455
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

