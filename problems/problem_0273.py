from pyler import EulerProblem


class Problem0273(EulerProblem):
    """
    Consider equations of the form: a2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer.
    For N=65 there are two solutions: a=1, b=8 and a=4, b=7. We call S(N) the
    sum of the values of a of all solutions of a2 + b2 = N, 0 ≤ a ≤ b, a, b and
    N integer. Thus S(65) = 1 + 4 = 5. Find ∑S(N), for all squarefree N only
    divisible by primes of the form 4k+1 with 4k+1 < 150.
    """
    problem_id = 273
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

