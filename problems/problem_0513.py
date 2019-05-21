from pyler import EulerProblem


class Problem0513(EulerProblem):
    """
    ABC is an integral sided triangle with sides a≤b≤c. mc is the median
    connecting C and the midpoint of AB.  F(n) is the number of such triangles
    with  c≤n for which mc has integral length as well. F(10)=3 and F(50)=165.
    Find F(100000).
    """
    problem_id = 513
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

