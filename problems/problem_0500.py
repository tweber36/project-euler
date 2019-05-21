from pyler import EulerProblem


class Problem0500(EulerProblem):
    """
    The number of divisors of 120 is 16. In fact 120 is the smallest number
    having 16 divisors.   Find the smallest number with 2500500 divisors. Give
    your answer modulo 500500507.
    """
    problem_id = 500
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

