from pyler import EulerProblem


class Problem0357(EulerProblem):
    """
    Consider the divisors of 30: 1,2,3,5,6,10,15,30. It can be seen that for
    every divisor d of 30, d+30/d is prime.   Find the sum of all positive
    integers n not exceeding 100 000 000such that for every divisor d of n,
    d+n/d is prime.
    """
    problem_id = 357
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

