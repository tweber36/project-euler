from pyler import EulerProblem


class Problem0258(EulerProblem):
    """
    A sequence is defined as:  gk = 1, for 0 ≤ k ≤ 1999 gk = gk-2000 + gk-1999,
    for k ≥ 2000. Find gk mod 20092010 for k = 1018.
    """
    problem_id = 258
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

