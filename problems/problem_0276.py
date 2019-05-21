from pyler import EulerProblem


class Problem0276(EulerProblem):
    """
    Consider the triangles with integer sides a, b and c with a ≤ b ≤ c. An
    integer sided triangle (a,b,c) is called primitive if  gcd(a,b,c)=1.  How
    many primitive integer sided triangles exist with a perimeter not exceeding
    10 000 000?
    """
    problem_id = 276
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

