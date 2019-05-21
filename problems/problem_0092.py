from pyler import EulerProblem


class Problem0092(EulerProblem):
    """
    A number chain is created by continuously adding the square of the digits in
    a number to form a new number until it has been seen before. For example, 44
    → 32 → 13 → 10 → 1 → 1 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
    Therefore any chain that arrives at 1 or 89 will become stuck in an endless
    loop. What is most amazing is that EVERY starting number will eventually
    arrive at 1 or 89. How many starting numbers below ten million will arrive
    at 89?
    """
    problem_id = 92
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
