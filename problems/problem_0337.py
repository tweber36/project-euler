from pyler import EulerProblem


class Problem0337(EulerProblem):
    """
    Let {a1, a2,..., an} be an integer sequence of length n such that: a1 = 6
    for all 1 ≤ i < n : φ(ai) < φ(ai+1) < ai < ai+11 Let S(N) be the number of
    such sequences with an ≤ N. For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9}
    and {6, 10}. We can verify that S(100) = 482073668 and S(10 000) mod 108 =
    73808307. Find S(20 000 000) mod 108. 1 φ denotes Euler's totient function.
    """
    problem_id = 337
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

