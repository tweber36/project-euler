from pyler import EulerProblem


class Problem0039(EulerProblem):
    """
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120. {20,48,52},
    {24,45,51}, {30,40,50} For which value of p ≤ 1000, is the number of
    solutions maximised?
    """
    problem_id = 39
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

