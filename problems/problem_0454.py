from pyler import EulerProblem


class Problem0454(EulerProblem):
    """
    In the following equation x, y, and n are positive integers. $$\dfrac{1}{x}
    + \dfrac{1}{y} = \dfrac{1}{n}$$ For a limit L we define F(L) as the number
    of solutions which satisfy x < y ≤ L. We can verify that F(15) = 4 and
    F(1000) = 1069. Find F(1012).
    """
    problem_id = 454
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

