from pyler import EulerProblem


class Problem0517(EulerProblem):
    """
    For every real number $a \gt 1$ is given the sequence $g_a$ by: $g_{a}(x)=1$
    for $x \lt a$ $g_{a}(x)=g_{a}(x-1)+g_a(x-a)$ for $x \ge a$  $G(n)=g_{\sqrt
    {n}}(n)$ $G(90)=7564511$.  Find $\sum G(p)$ for $p$ prime and $10000000 \lt
    p \lt 10010000$ Give your answer modulo 1000000007.
    """
    problem_id = 517
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

