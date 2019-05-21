from pyler import EulerProblem


class Problem0045(EulerProblem):
    """
    Triangle, pentagonal, and hexagonal numbers are generated by the following
    formulae: Triangle   Tn=n(n+1)/2   1, 3, 6, 10, 15, ... Pentagonal  
    Pn=n(3n−1)/2   1, 5, 12, 22, 35, ... Hexagonal   Hn=n(2n−1)   1, 6, 15, 28,
    45, ... It can be verified that T285 = P165 = H143 = 40755. Find the next
    triangle number that is also pentagonal and hexagonal.
    """
    problem_id = 45
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

