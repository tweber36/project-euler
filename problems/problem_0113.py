from pyler import EulerProblem


class Problem0113(EulerProblem):
    """
    Working from left-to-right if no digit is exceeded by the digit to its left
    it is called an increasing number; for example, 134468. Similarly if no
    digit is exceeded by the digit to its right it is called a decreasing
    number; for example, 66420. We shall call a positive integer that is neither
    increasing nor decreasing a "bouncy" number; for example, 155349. As n
    increases, the proportion of bouncy numbers below n increases such that
    there are only 12951 numbers below one-million that are not bouncy and only
    277032 non-bouncy numbers below 1010. How many numbers below a googol
    (10100) are not bouncy?
    """
    problem_id = 113
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

