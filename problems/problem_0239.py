from pyler import EulerProblem


class Problem0239(EulerProblem):
    """
    A set of disks numbered 1 through 100 are placed in a line in random order.
    What is the probability that we have a partial derangement such that exactly
    22 prime number discs are found away from their natural positions? (Any
    number of non-prime disks may also be found in or out of their natural
    positions.) Give your answer rounded to 12 places behind the decimal point
    in the form 0.abcdefghijkl.
    """
    problem_id = 239
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

