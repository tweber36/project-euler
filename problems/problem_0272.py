from pyler import EulerProblem


class Problem0272(EulerProblem):
    """
    For a positive number n, define C(n) as the number of the integers x, for
    which 1<x<n andx3≡1 mod n.   When n=91, there are 8 possible values for x,
    namely : 9, 16, 22, 29, 53, 74, 79, 81. Thus, C(91)=8.  Find the sum of the
    positive numbers n≤1011 for which C(n)=242.
    """
    problem_id = 272
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

