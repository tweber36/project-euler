from pyler import EulerProblem


class Problem0123(EulerProblem):
    """
    Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder
    when (pn−1)n + (pn+1)n is divided by pn2. For example, when n = 3, p3 = 5,
    and 43 + 63 = 280 ≡ 5 mod 25. The least value of n for which the remainder
    first exceeds 109 is 7037. Find the least value of n for which the remainder
    first exceeds 1010.
    """
    problem_id = 123
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

