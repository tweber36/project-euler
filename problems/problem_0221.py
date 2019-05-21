from pyler import EulerProblem


class Problem0221(EulerProblem):
    """
    We shall call a positive integer A an "Alexandrian integer", if there exist
    integers p, q, r such that:  A = p · q · r    and        1A =  1p +  1q +
    1r For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In
    fact, 630 is the 6th Alexandrian integer,  the first 6 Alexandrian integers
    being: 6, 42, 120, 156, 420 and 630. Find the 150000th Alexandrian integer.
    """
    problem_id = 221
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

