from pyler import EulerProblem


class Problem0487(EulerProblem):
    """
    Let fk(n) be the sum of the kth powers of the first n positive integers. For
    example, f2(10) = 12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385.
    Let Sk(n) be the sum of fk(i) for 1 ≤ i ≤ n. For example, S4(100) =
    35375333830. What is ∑ (S10000(1012) mod p) over all primes p between 2 ⋅
    109 and 2 ⋅ 109 + 2000?
    """
    problem_id = 487
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

