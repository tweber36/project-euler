from pyler import EulerProblem


class Problem0501(EulerProblem):
    """
    The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. The ten numbers
    not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56,
    66, 70, 78 and 88. Let f(n) be the count of numbers not exceeding n with
    exactly eight divisors. You are given f(100) = 10, f(1000) = 180 and
    f(106) = 224427. Find f(1012).
    """
    problem_id = 501
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

