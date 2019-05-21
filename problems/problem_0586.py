from pyler import EulerProblem


class Problem0586(EulerProblem):
    """
    The number 209 can be expressed as $a^2 + 3ab + b^2$ in two distinct ways:
    $ \qquad 209 = 8^2 + 3\cdot 8\cdot 5 + 5^2$  $ \qquad 209 = 13^2 +
    3\cdot13\cdot 1 + 1^2$   Let $f(n,r)$ be the number of integers $k$ not
    exceeding $n$ that can be expressed as $k=a^2 + 3ab + b^2$, with $a\gt b>0$
    integers, in exactly $r$ different ways.   You are given that $f(10^5, 4) =
    237$ and $f(10^8, 6) = 59517$.   Find $f(10^{15}, 40)$.
    """
    problem_id = 586
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

