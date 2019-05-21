from pyler import EulerProblem


class Problem0291(EulerProblem):
    """
    A prime number $p$ is called a Panaitopol prime if $p = \dfrac{x^4 -
    y^4}{x^3 + y^3}$ for some positive integers $x$ and $y$.  Find how many
    Panaitopol primes are less than 5×1015.
    """
    problem_id = 291
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

