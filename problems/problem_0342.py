from pyler import EulerProblem


class Problem0342(EulerProblem):
    """
    Consider the number 50. 502 = 2500 = 22 × 54, so φ(2500) = 2 × 4 × 53 = 8 ×
    53 = 23 × 53. 1 So 2500 is a square and  φ(2500) is a cube.   Find the sum
    of all numbers n, 1 < n < 1010 such that φ(n2) is a cube.   1 φ denotes
    Euler's totient function.
    """
    problem_id = 342
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

