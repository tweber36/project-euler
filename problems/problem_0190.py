from pyler import EulerProblem


class Problem0190(EulerProblem):
    """
    Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with x1
    + x2 + ... + xm = m for which Pm = x1 * x22 * ... * xmm is maximised. For
    example, it can be verified that [P10] = 4112 ([ ] is the integer part
    function). Find Σ[Pm] for 2 ≤ m ≤ 15.
    """
    problem_id = 190
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

