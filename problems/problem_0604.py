from pyler import EulerProblem


class Problem0604(EulerProblem):
    """
    Let $F(N)$ be the maximum number of lattice points in an axis-aligned
    $N\times N$ square that the graph of a single strictly convex increasing
    function can pass through.   You are given that $F(1) = 2$, $F(3) = 3$,
    $F(9) = 6$, $F(11) = 7$, $F(100) = 30$ and $F(50000) = 1898$.  Below is the
    graph of a function reaching the maximum 3 for $N=3$:     Find $F(10^{18})$.
    """
    problem_id = 604
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

