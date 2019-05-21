from pyler import EulerProblem


class Problem0512(EulerProblem):
    """
    Let $\varphi(n)$ be Euler's totient function. Let
    $f(n)=(\sum_{i=1}^{n}\varphi(n^i)) \text{ mod } (n+1)$. Let
    $g(n)=\sum_{i=1}^{n} f(i)$. $g(100)=2007$.   Find $g(5 \times 10^8)$.
    """
    problem_id = 512
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

