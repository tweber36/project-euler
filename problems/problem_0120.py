from pyler import EulerProblem


class Problem0120(EulerProblem):
    """
    Let r be the remainder when (a−1)n + (a+1)n is divided by a2. For example,
    if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies,
    so too will r, but for a = 7 it turns out that rmax = 42. For 3 ≤ a ≤ 1000,
    find ∑ rmax.
    """
    problem_id = 120
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

