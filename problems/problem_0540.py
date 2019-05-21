from pyler import EulerProblem


class Problem0540(EulerProblem):
    """
    A Pythagorean triple consists of three positive integers $a, b$ and $c$
    satisfying $a^2+b^2=c^2$. The triple is called primitive if $a, b$ and $c$
    are relatively prime. Let P($n$) be the number of primitive Pythagorean
    triples with $a < b < c \le n$. For example P(20) = 3, since there are three
    triples: (3,4,5), (5,12,13) and (8,15,17).   You are given that P(106) =
    159139. Find P(3141592653589793).
    """
    problem_id = 540
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

