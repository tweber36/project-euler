from pyler import EulerProblem


class Problem0131(EulerProblem):
    """
    There are some prime values, p, for which there exists a positive integer,
    n, such that the expression n3 + n2p is a perfect cube. For example, when p
    = 19, 83 + 82×19 = 123. What is perhaps most surprising is that for each
    prime with this property the value of n is unique, and there are only four
    such primes below one-hundred. How many primes below one million have this
    remarkable property?
    """
    problem_id = 131
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

