from pyler import EulerProblem


class Problem0160(EulerProblem):
    """
    For any N, let f(N) be the last five digits before the trailing zeroes in
    N!. For example, 9! = 362880 so f(9)=36288 10! = 3628800 so f(10)=36288 20!
    = 2432902008176640000 so f(20)=17664 Find f(1,000,000,000,000)
    """
    problem_id = 160
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

