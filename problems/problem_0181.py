from pyler import EulerProblem


class Problem0181(EulerProblem):
    """
    Having three black objects B and one white object W they can be grouped in 7
    ways like this: (BBBW)(B,BBW)(B,B,BW)(B,B,B,W) (B,BB,W)(BBB,W)(BB,BW) In how
    many ways can sixty black objects B and forty white objects W be  thus
    grouped?
    """
    problem_id = 181
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

