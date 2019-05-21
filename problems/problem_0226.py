from pyler import EulerProblem


class Problem0226(EulerProblem):
    """
    The blancmange curve is the set of points $(x, y)$ such that $0 \le x \le 1$
    and $y = \sum \limits_{n = 0}^{\infty} {\dfrac{s(2^n x)}{2^n}}$, where
    $s(x)$ is the distance from $x$ to the nearest integer. The area under the
    blancmange curve is equal to ½, shown in pink in the diagram below.   Let C
    be the circle with centre $\left ( \frac{1}{4}, \frac{1}{2} \right )$ and
    radius $\frac{1}{4}$, shown in black in the diagram. What area under the
    blancmange curve is enclosed by C?Give your answer rounded to eight decimal
    places in the form 0.abcdefgh
    """
    problem_id = 226
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

