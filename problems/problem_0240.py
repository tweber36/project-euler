from pyler import EulerProblem


class Problem0240(EulerProblem):
    """
    There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can
    be rolled so that the top three sum to 15. Some examples are:
    D1,D2,D3,D4,D5 = 4,3,6,3,5  D1,D2,D3,D4,D5 = 4,3,3,5,6  D1,D2,D3,D4,D5 =
    3,3,3,6,6  D1,D2,D3,D4,D5 = 6,6,3,3,3  In how many ways can twenty 12-sided
    dice (sides numbered 1 to 12) be rolled so that the top ten sum to 70?
    """
    problem_id = 240
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

