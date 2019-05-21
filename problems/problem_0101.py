from pyler import EulerProblem


class Problem0101(EulerProblem):
    """
    If we are presented with the first k terms of a sequence it is impossible to
    say with certainty the value of the next term, as there are infinitely many
    polynomial functions that can model the sequence. As an example, let us
    consider the sequence of cube numbers. This is defined by the generating
    function, un = n3: 1, 8, 27, 64, 125, 216, ... Suppose we were only given
    the first two terms of this sequence. Working on the principle that "simple
    is best" we should assume a linear relationship and predict the next term to
    be 15 (common difference 7). Even if we were presented with the first three
    terms, by the same principle of simplicity, a quadratic relationship should
    be assumed. We shall define OP(k, n) to be the nth term of the optimum
    polynomial generating function for the first k terms of a sequence. It
    should be clear that OP(k, n) will accurately generate the terms of the
    sequence for n ≤ k, and potentially the first incorrect term (FIT) will be
    OP(k, k+1); in which case we shall call it a bad OP (BOP). As a basis, if we
    were only given the first term of sequence, it would be most sensible to
    assume constancy; that is, for n ≥ 2, OP(1, n) = u1. Hence we obtain the
    following OPs for the cubic sequence:  OP(1, n) = 1 1, 1, 1, 1, ... OP(2, n)
    = 7n−6 1, 8, 15, ... OP(3, n) = 6n2−11n+6      1, 8, 27, 58, ... OP(4, n) =
    n3 1, 8, 27, 64, 125, ...  Clearly no BOPs exist for k ≥ 4. By considering
    the sum of FITs generated by the BOPs (indicated in red above), we obtain 1
    + 15 + 58 = 74. Consider the following tenth degree polynomial generating
    function: un = 1 − n + n2 − n3 + n4 − n5 + n6 − n7 + n8 − n9 + n10 Find the
    sum of FITs for the BOPs.
    """
    problem_id = 101
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

