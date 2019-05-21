from pyler import EulerProblem


class Problem0654(EulerProblem):
    """
    Let $T(n, m)$ be the number of $m$-tuples of positive integers such that the
    sum of any two neighbouring elements of the tuple is $\le n$.   For example,
    $T(3, 4)=8$, via the following eight $4$-tuples: $(1, 1, 1, 1)$ $(1, 1, 1,
    2)$ $(1, 1, 2, 1)$ $(1, 2, 1, 1)$ $(1, 2, 1, 2)$ $(2, 1, 1, 1)$ $(2, 1, 1,
    2)$ $(2, 1, 2, 1)$  You are also given that $T(5, 5)=246$, $T(10, 10^{2})
    \equiv 862820094 \pmod{1\,000\,000\,007}$ and  $T(10^2, 10) \equiv 782136797
    \pmod{1\,000\,000\,007}$.   Find $T(5000, 10^{12}) \bmod 1\,000\,000\,007$.
    """
    problem_id = 654
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

