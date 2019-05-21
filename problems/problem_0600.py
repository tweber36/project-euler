from pyler import EulerProblem


class Problem0600(EulerProblem):
    """
    Let H(n) be the number of distinct integer sided equiangular convex hexagons
    with perimeter not exceeding n. Hexagons are distinct if and only if they
    are not congruent. You are given H(6) = 1, H(12) = 10, H(100) = 31248. Find
    H(55106).  Equiangular hexagons with perimeter not exceeding 12
    """
    problem_id = 600
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

