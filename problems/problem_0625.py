from pyler import EulerProblem


class Problem0625(EulerProblem):
    """
    $G(N)=\sum_{j=1}^N\sum_{i=1}^j \text{gcd}(i,j)$.  You are given:
    $G(10)=122$.  Find $G(10^{11})$. Give your answer modulo 998244353
    """
    problem_id = 625
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

