from pyler import EulerProblem


class Problem0548(EulerProblem):
    """
    A gozinta chain for n is a sequence {1,a,b,...,n} where each element
    properly divides the next. There are eight gozinta chains for 12: {1,12}
    ,{1,2,12}, {1,2,4,12}, {1,2,6,12}, {1,3,12}, {1,3,6,12}, {1,4,12} and
    {1,6,12}.  Let g(n) be the number of gozinta chains for n, so g(12)=8.
    g(48)=48 and g(120)=132.   Find the sum of the numbers n  not exceeding 1016
    for which g(n)=n.
    """
    problem_id = 548
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

