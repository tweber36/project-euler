from pyler import EulerProblem


class Problem0581(EulerProblem):
    """
    A number is p-smooth if it has no prime factors larger than p. Let T be the
    sequence of triangular numbers, ie T(n)=n(n+1)/2. Find the sum of all
    indices n such that T(n) is 47-smooth.
    """
    problem_id = 581
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

