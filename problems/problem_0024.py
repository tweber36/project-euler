from pyler import EulerProblem


class Problem0024(EulerProblem):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
    are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120 
     201   210 What is the millionth lexicographic permutation of the digits 0,
    1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    problem_id = 24
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

