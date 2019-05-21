from pyler import EulerProblem


class Problem0634(EulerProblem):
    """
    Define $F(n)$ to be the number of integers $x≤n$ that can be written in the
    form $x=a^2b^3$, where $a$ and $b$ are integers not necessarily different
    and both greater than 1.  For example, $32=2^2\times 2^3$  and $72=3^2\times
    2^3$ are the only two integers less than 100 that can be written in this
    form. Hence, $F(100)=2$.   Further you are given $F(2\times 10^4)=130$ and
    $F(3\times 10^6)=2014$.   Find $F(9\times 10^{18})$.
    """
    problem_id = 634
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

