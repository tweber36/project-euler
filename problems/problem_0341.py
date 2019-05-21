from pyler import EulerProblem


class Problem0341(EulerProblem):
    """
    The Golomb's self-describing sequence {G(n)} is the only nondecreasing
    sequence of natural numbers such that n appears exactly G(n) times in the
    sequence. The values of G(n) for the first few n are
    n123456789101112131415…G(n)122334445556666… You are given that G(103) = 86,
    G(106) = 6137. You are also given that ΣG(n3) = 153506976 for 1 ≤ n < 103.
    Find ΣG(n3) for 1 ≤ n < 106.
    """
    problem_id = 341
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

