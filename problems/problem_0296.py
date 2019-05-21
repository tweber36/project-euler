from pyler import EulerProblem


class Problem0296(EulerProblem):
    """
    Given is an integer sided triangle ABC with BC ≤ AC ≤ AB.k is the angular
    bisector of angle ACB.m is the tangent at C to the circumscribed circle of
    ABC.n is a line parallel to m through B. The intersection of n and k is
    called E.    How many triangles ABC with a perimeter not exceeding 100 000
    exist such that BE has integral length?
    """
    problem_id = 296
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

