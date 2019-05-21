from pyler import EulerProblem


class Problem0435(EulerProblem):
    """
    The Fibonacci numbers {fn, n ≥ 0} are defined recursively as fn = fn-1 +
    fn-2 with base cases f0 = 0 and f1 = 1. Define the polynomials {Fn, n ≥ 0}
    as Fn(x) = ∑fixi for 0 ≤ i ≤ n. For example, F7(x) = x + x2 + 2x3 + 3x4 +
    5x5 + 8x6 + 13x7, and F7(11) = 268357683. Let n = 1015. Find the sum
    [∑0≤x≤100 Fn(x)] mod 1307674368000 (= 15!).
    """
    problem_id = 435
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
