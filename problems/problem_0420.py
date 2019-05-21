from pyler import EulerProblem


class Problem0420(EulerProblem):
    """
    A positive integer matrix is a matrix whose elements are all positive
    integers. Some positive integer matrices can be expressed as a square of a
    positive integer matrix in two different ways. Here is an example:
    $$\begin{pmatrix} 40 & 12\\ 48 & 40 \end{pmatrix} = \begin{pmatrix} 2 & 3\\
    12 & 2 \end{pmatrix}^2 = \begin{pmatrix} 6 & 1\\ 4 & 6 \end{pmatrix}^2 $$
    We define F(N) as the number of the 2x2 positive integer matrices which have
    a trace less than N and which can be expressed as a square of a positive
    integer matrix in two different ways. We can verify that F(50) = 7 and
    F(1000) = 1019.   Find F(107).
    """
    problem_id = 420
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

