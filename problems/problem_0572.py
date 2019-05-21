from pyler import EulerProblem


class Problem0572(EulerProblem):
    """
    A matrix $M$ is called idempotent if $M^2 = M$. Let $M$ be a three by three
    matrix :  $M=\begin{pmatrix}    a & b & c\\    d & e & f\\   g &h &i\\
    \end{pmatrix}$. Let C(n) be the number of  idempotent three by three
    matrices $M$ with integer elements such that $ -n \le a,b,c,d,e,f,g,h,i \le
    n$.  C(1)=164 and C(2)=848.   Find C(200).
    """
    problem_id = 572
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

