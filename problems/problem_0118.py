from pyler import EulerProblem


class Problem0118(EulerProblem):
    """
    Using all of the digits 1 through 9 and concatenating them freely to form
    decimal integers, different sets can be formed. Interestingly with the set
    {2,5,47,89,631}, all of the elements belonging to it are prime. How many
    distinct sets containing each of the digits one through nine exactly once
    contain only prime elements?
    """
    problem_id = 118
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

