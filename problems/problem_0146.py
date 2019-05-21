from pyler import EulerProblem


class Problem0146(EulerProblem):
    """
    The smallest positive integer n for which the numbers n2+1, n2+3, n2+7,
    n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such
    integers n below one-million is 1242490. What is the sum of all such
    integers n below 150 million?
    """
    problem_id = 146
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

