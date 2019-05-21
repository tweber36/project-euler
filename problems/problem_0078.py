from pyler import EulerProblem


class Problem0078(EulerProblem):
    """
    Let p(n) represent the number of different ways in which n coins can be
    separated into piles. For example, five coins can be separated into piles in
    exactly seven different ways, so p(5)=7.  OOOOO OOOO   O OOO   OO OOO   O 
     O OO   OO   O OO   O   O   O O   O   O   O   O  Find the least value of n
    for which p(n) is divisible by one million.
    """
    problem_id = 78
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

