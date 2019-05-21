from pyler import EulerProblem


class Problem0390(EulerProblem):
    """
    Consider the triangle with sides √5, √65 and √68. It can be shown that this
    triangle has area 9. S(n) is the sum of the areas of  all triangles with
    sides √(1+b2), √(1+c2) and √(b2+c2) (for positive integers b and c ) that
    have an integral area not exceeding n. The example triangle has b=2 and c=8.
    S(106)=18018206. Find S(1010).
    """
    problem_id = 390
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

