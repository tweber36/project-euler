from pyler import EulerProblem


class Problem0662(EulerProblem):
    """
    Alice walks on a lattice grid. She can step from one lattice point $A (a,b)$
    to another $B (a+x,b+y)$ providing distance $AB = \sqrt{x^2+y^2}$ is a
    Fibonacci number $\{1,2,3,5,8,13,\ldots\}$ and $x\ge 0,$  $y\ge 0$.    In
    the lattice grid below Alice can step from the blue point to any of the red
    points.   Let $F(W,H)$ be the number of paths Alice can take from $(0,0)$ to
    $(W,H)$. You are given $F(3,4) = 278$ and $F(10,10) = 215846462$.   Find
    $F(10\,000,10\,000) \bmod 1\,000\,000\,007$.
    """
    problem_id = 662
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

