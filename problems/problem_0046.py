from pyler import EulerProblem


class Problem0046(EulerProblem):
    """
    It was proposed by Christian Goldbach that every odd composite number can be
    written as the sum of a prime and twice a square. 9 = 7 + 2×12 15 = 7 + 2×22
    21 = 3 + 2×32 25 = 7 + 2×32 27 = 19 + 2×22 33 = 31 + 2×12 It turns out that
    the conjecture was false. What is the smallest odd composite that cannot be
    written as the sum of a prime and twice a square?
    """
    problem_id = 46
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

