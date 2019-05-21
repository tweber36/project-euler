from pyler import EulerProblem


class Problem0356(EulerProblem):
    """
    Let an be the largest real root of a polynomial g(x) = x3 - 2n·x2 + n. For
    example, a2 = 3.86619826...  Find the last eight digits of $\sum \limits_{i
    = 1}^{30} {\left \lfloor a_i^{987654321} \right \rfloor}$.  Note: $\lfloor a
    \rfloor$ represents the floor function.
    """
    problem_id = 356
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

