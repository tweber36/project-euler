from pyler import EulerProblem


class Problem0612(EulerProblem):
    """
    Let's call two numbers  friend numbers if their representation in base 10
    has at least one common digit. E.g. 1123 and 3981 are friend numbers.    Let
    $f(n)$ be the number of pairs $(p,q)$ with $1\le p \lt q \lt n$ such that
    $p$ and $q$ are friend numbers. $f(100)=1539$.   Find $f(10^{18})$ mod
    $1000267129$.
    """
    problem_id = 612
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

