from pyler import EulerProblem


class Problem0516(EulerProblem):
    """
    5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
    5-smooth numbers are also called Hamming numbers. Let S(L) be the sum of the
    numbers n not exceeding L such that Euler's totient function φ(n) is a
    Hamming number. S(100)=3728.   Find S(1012). Give your answer modulo 232.
    """
    problem_id = 516
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

