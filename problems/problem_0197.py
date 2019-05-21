from pyler import EulerProblem


class Problem0197(EulerProblem):
    """
    Given is the function f(x) = ⌊230.403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the floor-
    function), the sequence un is defined by u0 = -1 and un+1 = f(un). Find un +
    un+1 for n = 1012. Give your answer with 9 digits after the decimal point.
    """
    problem_id = 197
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

