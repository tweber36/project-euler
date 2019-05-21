from pyler import EulerProblem


class Problem0526(EulerProblem):
    """
    Let f(n) be the largest prime factor of n. Let g(n) = f(n) + f(n+1) + f(n+2)
    + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8), the sum of the
    largest prime factor of each of nine consecutive numbers starting with n.
    Let h(n) be the maximum value of g(k) for 2 ≤ k ≤ n. You are given: f(100) =
    5 f(101) = 101 g(100) = 409 h(100) = 417 h(109) = 4896292593Find h(1016).
    """
    problem_id = 526
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

