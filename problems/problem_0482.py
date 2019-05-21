from pyler import EulerProblem


class Problem0482(EulerProblem):
    """
    ABC is an integer sided triangle with incenter I and perimeter p. The
    segments IA, IB and IC have integral length as well.    Let L = p + |IA| +
    |IB| + |IC|.    Let S(P) = ∑L for all such triangles where p ≤ P. For
    example, S(103) = 3619.   Find S(107).
    """
    problem_id = 482
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

