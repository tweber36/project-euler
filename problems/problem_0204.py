from pyler import EulerProblem


class Problem0204(EulerProblem):
    """
    A Hamming number is a positive number which has no prime factor larger than
    5. So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
    There are 1105 Hamming numbers not exceeding 108. We will call a positive
    number a generalised Hamming number of type n, if it has no prime factor
    larger than n. Hence the Hamming numbers are the generalised Hamming numbers
    of type 5. How many generalised Hamming numbers of type 100 are there which
    don't exceed 109?
    """
    problem_id = 204
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

