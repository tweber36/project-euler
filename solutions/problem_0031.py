from pyler.pyler import EulerProblem


class Problem0031(EulerProblem):
    """
    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1
    (100p), and £2 (200p). It is possible to make £2 in the following way: 1×£1
    + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p How many different ways can £2 be made
    using any number of coins?
    """
    problem_id = 31
    simple_input = 0
    simple_output = 1
    real_input = 0

    def solver(self, input_val):
        raise NotImplementedError


if __name__ == '__main__':
    import unittest
    unittest.main()

