from pyler import EulerProblem


class Problem0608(EulerProblem):
    """
    Let $D(m,n)=\displaystyle\sum_{d|m}\sum_{k=1}^n\sigma_{\small 0}(kd)$ where
    $d$ runs through all divisors of $m$ and $\sigma_{\small 0}(n)$ is the
    number of divisors of $n$. You are given $D(3!,10^2)=3398$ and
    $D(4!,10^6)=268882292$. Find $D(200!,10^{12}) \text{ mod } (10^9 + 7)$.
    """
    problem_id = 608
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

