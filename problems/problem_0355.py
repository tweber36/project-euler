from pyler import EulerProblem


class Problem0355(EulerProblem):
    """
    Define Co(n) to be the maximal possible sum of a set of mutually co-prime
    elements from {1, 2, ..., n}. For example Co(10) is 30 and hits that maximum
    on the subset {1, 5, 7, 8, 9}.   You are given that Co(30) = 193 and Co(100)
    = 1356.   Find Co(200000).
    """
    problem_id = 355
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

