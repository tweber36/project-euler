from pyler import EulerProblem


class Problem0626(EulerProblem):
    """
    A binary matrix is a matrix consisting entirely of 0s and 1s. Consider the
    following transformations that can be performed on a binary matrix: Swap any
    two rows Swap any two columns Flip all elements in a single row (1s become
    0s, 0s become 1s) Flip all elements in a single column Two binary matrices
    $A$ and $B$ will be considered equivalent if there is a sequence of such
    transformations that when applied to $A$ yields $B$. For example, the
    following two matrices are equivalent: $A=\begin{pmatrix}    1 & 0 & 1 \\
    0 & 0 & 1 \\   0 & 0 & 0 \\ \end{pmatrix} \quad B=\begin{pmatrix}    0 & 0 &
    0 \\    1 & 0 & 0 \\   0 & 0 & 1 \\ \end{pmatrix}$ via the sequence of two
    transformations "Flip all elements in column 3" followed by "Swap rows 1 and
    2". Define $c(n)$ to be the maximum number of $n\times n$ binary matrices
    that can be found such that no two are equivalent. For example, $c(3)=3$.
    You are also given that $c(5)=39$ and $c(8)=656108$. Find $c(20)$, and give
    your answer modulo $1\,001\,001\,011$.
    """
    problem_id = 626
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

