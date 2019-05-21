from pyler import EulerProblem


class Problem0407(EulerProblem):
    """
    If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.   The largest
    value of a such that a2 ≡ a mod 6 is 4. Let's call M(n) the largest value of
    a < n such that a2 ≡ a (mod n). So M(6) = 4.   Find ∑M(n) for 1 ≤ n ≤ 107.
    """
    problem_id = 407
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

