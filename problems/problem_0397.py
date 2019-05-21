from pyler import EulerProblem


class Problem0397(EulerProblem):
    """
    On the parabola y = x2/k, three points A(a, a2/k), B(b, b2/k) and C(c, c2/k)
    are chosen.   Let F(K, X) be the number of the integer quadruplets (k, a, b,
    c) such that at least one angle of the triangle ABC is 45-degree, with 1 ≤ k
    ≤ K and -X ≤ a < b < c ≤ X.   For example, F(1, 10) = 41 and F(10, 100) =
    12492. Find F(106, 109).
    """
    problem_id = 397
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

