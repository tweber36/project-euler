from pyler import EulerProblem


class Problem0496(EulerProblem):
    """
    Given an integer sided triangle ABC: Let I be the incenter of ABC. Let D be
    the intersection between the line AI and the circumcircle of ABC (A ≠ D). We
    define F(L) as the sum of BC for the triangles ABC that satisfy AC = DI and
    BC ≤ L. For example, F(15) = 45 because the triangles ABC with (BC,AC,AB) =
    (6,4,5), (12,8,10), (12,9,7), (15,9,16) satisfy the conditions. Find F(109).
    """
    problem_id = 496
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

