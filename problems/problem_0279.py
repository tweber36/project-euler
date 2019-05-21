from pyler import EulerProblem


class Problem0279(EulerProblem):
    """
    How many triangles are there with integral sides, at least one integral
    angle (measured in degrees), and a perimeter that does not exceed 108?
    """
    problem_id = 279
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

