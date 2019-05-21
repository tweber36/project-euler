from pyler import EulerProblem


class Problem0642(EulerProblem):
    """
    Let $f(n)$ be the largest prime factor of $n$ and $\displaystyle F(n) =
    \sum_{i=2}^{n}f(i)$. For example $F(10)=32$, $F(100)=1915$ and
    $F(10000)=10118280$.  Find $F(201820182018)$. Give your answer modulus
    $10^9$.
    """
    problem_id = 642
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

