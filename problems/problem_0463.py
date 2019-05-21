from pyler import EulerProblem


class Problem0463(EulerProblem):
    """
    The function $f$ is defined for all positive integers as follows: $f(1)=1$
    $f(3)=3$ $f(2n)=f(n)$ $f(4n + 1)=2f(2n + 1) - f(n)$ $f(4n + 3)=3f(2n + 1) -
    2f(n)$  The function $S(n)$ is defined as $\sum_{i=1}^{n}f(i)$. $S(8)=22$
    and $S(100)=3604$. Find $S(3^{37})$. Give the last 9 digits of your answer.
    """
    problem_id = 463
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

