from pyler import EulerProblem


class Problem0271(EulerProblem):
    """
    For a positive number n, define S(n) as the sum of the integers x, for which
    1<x<n andx3≡1 mod n.   When n=91, there are 8 possible values for x, namely
    : 9, 16, 22, 29, 53, 74, 79, 81. Thus, S(91)=9+16+22+29+53+74+79+81=363.
    Find S(13082761331670030).
    """
    problem_id = 271
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

