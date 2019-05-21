from pyler import EulerProblem


class Problem0466(EulerProblem):
    """
    Let P(m,n) be the number of distinct terms in an m×n multiplication table.
    For example, a 3×4 multiplication table looks like this: × 12341 12342 24683
    36912 There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.
    You are given that: P(64,64) = 1263, P(12,345) = 1998, and P(32,1015) =
    13826382602124302. Find P(64,1016).
    """
    problem_id = 466
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

