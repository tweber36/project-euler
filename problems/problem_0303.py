from pyler import EulerProblem


class Problem0303(EulerProblem):
    """
    For a positive integer n, define f(n) as the least positive multiple of n
    that, written in base 10, uses only digits ≤ 2. Thus f(2)=2, f(3)=12,
    f(7)=21, f(42)=210, f(89)=1121222. Also, $\sum \limits_{n = 1}^{100}
    {\dfrac{f(n)}{n}} = 11363107$.  Find $\sum \limits_{n=1}^{10000}
    {\dfrac{f(n)}{n}}$.
    """
    problem_id = 303
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

