from pyler import EulerProblem


class Problem0554(EulerProblem):
    """
    On a chess board, a centaur moves like a king or a knight. The diagram below
    shows the valid moves of a centaur (represented by an inverted king) on an
    8x8 board.  It can be shown that at most n2 non-attacking centaurs can be
    placed on a board of size 2n×2n. Let C(n) be the number of ways to place n2
    centaurs on a 2n×2n board so that no centaur attacks another directly. For
    example C(1) = 4, C(2) = 25, C(10) = 1477721. Let Fi be the ith Fibonacci
    number defined as F1 = F2 = 1 and Fi = Fi-1 + Fi-2 for i > 2. Find
    $\displaystyle \left( \sum_{i=2}^{90} C(F_i) \right) \text{mod } (10^8+7)$.
    """
    problem_id = 554
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

