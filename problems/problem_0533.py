from pyler import EulerProblem


class Problem0533(EulerProblem):
    """
    The Carmichael function λ(n) is defined as the smallest positive integer m
    such that am = 1 modulo n for all integers a coprime with n. For example
    λ(8) = 2 and λ(240) = 4. Define L(n) as the smallest positive integer m such
    that λ(k) ≥ n for all k ≥ m. For example, L(6) = 241 and
    L(100) = 20 174 525 281. Find L(20 000 000). Give the last 9 digits of your
    answer.
    """
    problem_id = 533
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

