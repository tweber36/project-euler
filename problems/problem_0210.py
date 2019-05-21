from pyler import EulerProblem


class Problem0210(EulerProblem):
    """
    Consider the set S(r) of points (x,y) with integer coordinates satisfying
    |x| + |y| ≤ r.  Let O be the point (0,0) and C the point (r/4,r/4).  Let
    N(r) be the number of points B in S(r), so that the triangle OBC has an
    obtuse angle, i.e. the largest angle α satisfies 90°<α<180°. So, for
    example, N(4)=24 and N(8)=100.  What is N(1,000,000,000)?
    """
    problem_id = 210
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

