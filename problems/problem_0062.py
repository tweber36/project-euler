from pyler import EulerProblem


class Problem0062(EulerProblem):
    """
    The cube, 41063625 (3453), can be permuted to produce two other cubes:
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
    which has exactly three permutations of its digits which are also cube. Find
    the smallest cube for which exactly five permutations of its digits are
    cube.
    """
    problem_id = 62
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

