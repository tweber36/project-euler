from pyler import EulerProblem


class Problem0372(EulerProblem):
    """
    Let $R(M, N)$ be the number of lattice points $(x, y)$ which satisfy
    $M\!\lt\!x\!\le\!N$, $M\!\lt\!y\!\le\!N$ and
    $\large\left\lfloor\!\frac{y^2}{x^2}\!\right\rfloor$ is odd. We can verify
    that $R(0, 100) = 3019$ and $R(100, 10000) = 29750422$. Find $R(2\cdot10^6,
    10^9)$.   Note: $\lfloor x\rfloor$ represents the floor function.
    """
    problem_id = 372
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

