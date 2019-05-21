from pyler import EulerProblem


class Problem0148(EulerProblem):
    """
    We can easily verify that none of the entries in the first seven rows of
    Pascal's triangle are divisible by 7:              1            1    1     
       1    2    1        1    3    3    1      1    4    6    4    1    1    5
     10   10    5    1 1    6   15   20   15    6    1 However, if we check the
    first one hundred rows, we will find that only 2361 of the 5050 entries are
    not divisible by 7. Find the number of entries which are not divisible by 7
    in the first one billion (109) rows of Pascal's triangle.
    """
    problem_id = 148
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

