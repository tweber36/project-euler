from pyler import EulerProblem


class Problem0234(EulerProblem):
    """
    For an integer n ≥ 4, we define the lower prime square root of n, denoted by
    lps(n), as the largest prime ≤ √n and the upper prime square root of n,
    ups(n), as the smallest prime ≥ √n. So, for example, lps(4) = 2 = ups(4),
    lps(1000) = 31, ups(1000) = 37. Let us call an integer n ≥ 4 semidivisible,
    if one of lps(n) and ups(n) divides n, but not both. The sum of the
    semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
    15 is not semidivisible because it is a multiple of both lps(15) = 3 and
    ups(15) = 5. As a further example, the sum of the 92 semidivisible numbers
    up to 1000 is 34825. What is the sum of all semidivisible numbers not
    exceeding 999966663333 ?
    """
    problem_id = 234
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

