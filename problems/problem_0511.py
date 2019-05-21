from pyler import EulerProblem


class Problem0511(EulerProblem):
    """
    Let Seq(n,k) be the number of positive-integer sequences {ai}1≤i≤n of length
    n such that: n is divisible by ai for 1 ≤ i ≤ n, and n + a1 + a2 + ... + an
    is divisible by k. Examples: Seq(3,4) = 4, and the 4 sequences are: {1, 1,
    3} {1, 3, 1} {3, 1, 1} {3, 3, 3} Seq(4,11) = 8, and the 8 sequences are: {1,
    1, 1, 4} {1, 1, 4, 1} {1, 4, 1, 1} {4, 1, 1, 1} {2, 2, 2, 1} {2, 2, 1, 2}
    {2, 1, 2, 2} {1, 2, 2, 2} The last nine digits of Seq(1111,24) are
    840643584. Find the last nine digits of Seq(1234567898765,4321).
    """
    problem_id = 511
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

