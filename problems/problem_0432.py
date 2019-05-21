from pyler import EulerProblem


class Problem0432(EulerProblem):
    """
    Let S(n,m) = ∑φ(n × i) for 1 ≤ i ≤ m. (φ is Euler's totient function) You
    are given that S(510510,106 )= 45480596821125120.    Find S(510510,1011).
    Give the last 9 digits of your answer.
    """
    problem_id = 432
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

