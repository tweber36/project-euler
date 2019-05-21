from pyler import EulerProblem


class Problem0170(EulerProblem):
    """
    Take the number 6 and multiply it by each of 1273 and 9854: 6 × 1273 =  7638
    6 × 9854 = 59124 By concatenating these products we get the 1 to 9
    pandigital 763859124. We will call 763859124 the "concatenated product of 6
    and (1273,9854)". Notice too, that the concatenation of the input numbers,
    612739854, is also 1 to 9 pandigital. The same can be done for 0 to 9
    pandigital numbers. What is the largest 0 to 9 pandigital 10-digit
    concatenated product of an integer with two or more other integers, such
    that the concatenation of the input numbers is also a 0 to 9 pandigital
    10-digit number?
    """
    problem_id = 170
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

