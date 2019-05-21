from pyler import EulerProblem


class Problem0536(EulerProblem):
    """
    Let S(n) be the sum of all positive integers m not exceeding n having the
    following property:a m+4 ≡ a (mod m) for all integers a.   The values of m ≤
    100 that satisfy this property are 1, 2, 3, 5 and 21, thus S(100) =
    1+2+3+5+21 = 32. You are given S(106) = 22868117.   Find S(1012).
    """
    problem_id = 536
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

