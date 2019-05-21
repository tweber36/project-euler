from pyler import EulerProblem


class Problem0307(EulerProblem):
    """
    k defects are randomly distributed amongst n integrated-circuit chips
    produced by a factory (any number of defects may be found on a chip and each
    defect is independent of the other defects).   Let p(k,n) represent the
    probability that there is a chip with at least 3 defects. For instance
    p(3,7) ≈ 0.0204081633.   Find p(20 000, 1 000 000) and give your answer
    rounded to 10 decimal places in the form 0.abcdefghij
    """
    problem_id = 307
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

