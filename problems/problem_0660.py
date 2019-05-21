from pyler import EulerProblem


class Problem0660(EulerProblem):
    """
    We call an integer sided triangle $n$-pandigital if it contains one angle of
    120 degrees and, when the sides of the triangle are written in base $n$,
    together they use all $n$ digits of that base exactly once.  For example,
    the triangle (217, 248, 403) is 9-pandigital because it contains one angle
    of 120 degrees and the sides written in base 9 are $261_9, 305_9, 487_9$
    using each of the 9 digits of that base once. Find the sum of the largest
    sides of all n-pandigital triangles with $9 \le n \le 18$.
    """
    problem_id = 660
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

