from pyler import EulerProblem


class Problem0627(EulerProblem):
    """
    Consider the set $S$ of all possible products of $n$ positive integers not
    exceeding $m$, that is  $S=\{ x_1x_2\dots x_n \, | \, 1 \le x_1, x_2, ...,
    x_n \le m \}$.  Let $F(m,n)$ be the number of the distinct elements of the
    set $S$. For example, $F(9, 2) = 36$ and $F(30,2)=308$. Find $F(30,
    10001)\text{ mod }1\,000\,000\,007$.
    """
    problem_id = 627
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

