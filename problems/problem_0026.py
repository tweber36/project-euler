from pyler import EulerProblem


class Problem0026(EulerProblem):
    """
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:  1/2= 0.5 1/3= 0.(3)
    1/4= 0.25 1/5= 0.2 1/6= 0.1(6) 1/7= 0.(142857) 1/8= 0.125 1/9= 0.(1)
    1/10= 0.1  Where 0.1(6) means 0.166666..., and has a 1-digit recurring
    cycle. It can be seen that 1/7 has a 6-digit recurring cycle. Find the value
    of d < 1000 for which 1/d contains the longest recurring cycle in its
    decimal fraction part.
    """
    problem_id = 26
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

