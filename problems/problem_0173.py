from pyler import EulerProblem


class Problem0173(EulerProblem):
    """
    We shall define a square lamina to be a square outline with a square "hole"
    so that the shape possesses vertical and horizontal symmetry. For example,
    using exactly thirty-two square tiles we can form two different square
    laminae:   With one-hundred tiles, and not necessarily using all of the
    tiles at one time, it is possible to form forty-one different square
    laminae. Using up to one million tiles how many different square laminae can
    be formed?
    """
    problem_id = 173
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

