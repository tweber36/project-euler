from pyler import EulerProblem


class Problem0108(EulerProblem):
    """
    In the following equation x, y, and n are positive integers. $$\dfrac{1}{x}
    + \dfrac{1}{y} = \dfrac{1}{n}$$ For n = 4 there are exactly three distinct
    solutions: $$\begin{align} \dfrac{1}{5} + \dfrac{1}{20} &= \dfrac{1}{4}\\
    \dfrac{1}{6} + \dfrac{1}{12} &= \dfrac{1}{4}\\ \dfrac{1}{8} + \dfrac{1}{8}
    &= \dfrac{1}{4} \end{align} $$  What is the least value of n for which the
    number of distinct solutions exceeds one-thousand? NOTE: This problem is an
    easier version of Problem 110; it is strongly advised that you solve this
    one first.
    """
    problem_id = 108
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

