from pyler import EulerProblem


class Problem0132(EulerProblem):
    """
    A number consisting entirely of ones is called a repunit. We shall define
    R(k) to be a repunit of length k. For example, R(10) = 1111111111 =
    11×41×271×9091, and the sum of these prime factors is 9414. Find the sum of
    the first forty prime factors of R(109).
    """
    problem_id = 132
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

