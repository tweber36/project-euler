from pyler import EulerProblem


class Problem0129(EulerProblem):
    """
    A number consisting entirely of ones is called a repunit. We shall define
    R(k) to be a repunit of length k; for example, R(6) = 111111. Given that n
    is a positive integer and GCD(n, 10) = 1, it can be shown that there always
    exists a value, k, for which R(k) is divisible by n, and let A(n) be the
    least such value of k; for example, A(7) = 6 and A(41) = 5. The least value
    of n for which A(n) first exceeds ten is 17. Find the least value of n for
    which A(n) first exceeds one-million.
    """
    problem_id = 129
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

