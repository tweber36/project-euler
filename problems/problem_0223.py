from pyler import EulerProblem


class Problem0223(EulerProblem):
    """
    Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if
    the sides satisfy a2 + b2 = c2 + 1. How many barely acute triangles are
    there with perimeter ≤ 25,000,000?
    """
    problem_id = 223
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

