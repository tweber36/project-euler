from pyler import EulerProblem


class Problem0205(EulerProblem):
    """
    Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
    3, 4. Colin has six six-sided (cubic) dice, each with faces numbered 1, 2,
    3, 4, 5, 6. Peter and Colin roll their dice and compare totals: the highest
    total wins. The result is a draw if the totals are equal. What is the
    probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded
    to seven decimal places in the form 0.abcdefg
    """
    problem_id = 205
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

