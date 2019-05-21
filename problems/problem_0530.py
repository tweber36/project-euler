from pyler import EulerProblem


class Problem0530(EulerProblem):
    """
    Every divisor d of a number n has a complementary divisor n/d. Let f(n) be
    the sum of the greatest common divisor of d and n/d over all positive
    divisors d of n, that is $f(n)=\displaystyle\sum\limits_{d|n}\,
    \text{gcd}(d,\frac n d)$. Let F be the summatory function of f, that is
    $F(k)=\displaystyle\sum\limits_{n=1}^k \, f(n)$. You are given that F(10)=32
    and F(1000)=12776. Find F(1015).
    """
    problem_id = 530
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

