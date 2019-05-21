from pyler import EulerProblem


class Problem0225(EulerProblem):
    """
    The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ... is
    defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.   It can be shown
    that 27 does not divide any terms of this sequence.In fact, 27 is the first
    odd number with this property.  Find the 124th odd number that does not
    divide any terms of the above sequence.
    """
    problem_id = 225
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

