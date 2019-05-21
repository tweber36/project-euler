from pyler import EulerProblem


class Problem0521(EulerProblem):
    """
    Let smpf(n) be the smallest prime factor of n. smpf(91)=7 because 91=7×13
    and smpf(45)=3 because 45=3×3×5. Let S(n) be the sum of smpf(i) for 2 ≤ i ≤
    n. E.g. S(100)=1257.   Find S(1012) mod 109.
    """
    problem_id = 521
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

