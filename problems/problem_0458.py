from pyler import EulerProblem


class Problem0458(EulerProblem):
    """
    Consider the alphabet A made out of the letters of the word "project":
    A={c,e,j,o,p,r,t}. Let T(n) be the number of strings of length n consisting
    of letters from A that do not have a substring that is one of the 5040
    permutations of "project".  T(7)=77-7!=818503.   Find T(1012). Give the last
    9 digits of your answer.
    """
    problem_id = 458
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

