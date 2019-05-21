from pyler import EulerProblem


class Problem0452(EulerProblem):
    """
    Define F(m,n) as the number of n-tuples of positive integers for which the
    product of the elements doesn't exceed m. F(10, 10) = 571. F(106, 106) mod
    1 234 567 891 = 252903833. Find F(109, 109) mod 1 234 567 891.
    """
    problem_id = 452
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

