from pyler import EulerProblem


class Problem0354(EulerProblem):
    """
    Consider a honey bee's honeycomb where each cell is a perfect regular
    hexagon with side length 1.    One particular cell is occupied by the queen
    bee. For a positive real number L, let B(L) count the cells with distance L
    from the queen bee cell (all distances are measured from centre to centre);
    you may assume that the honeycomb is large enough to accommodate for any
    distance we wish to consider.  For example, B(√3) = 6, B(√21) = 12 and B(111
    111 111) = 54. Find the number of L ≤ 5·1011 such that B(L) = 450.
    """
    problem_id = 354
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

