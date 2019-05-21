from pyler import EulerProblem


class Problem0362(EulerProblem):
    """
    Consider the number 54. 54 can be factored in 7 distinct ways into one or
    more factors larger than 1: 54, 2×27, 3×18, 6×9, 3×3×6, 2×3×9 and 2×3×3×3.
    If we require that the factors are all squarefree only two ways remain:
    3×3×6 and 2×3×3×3.   Let's call Fsf(n) the number of ways n can be factored
    into one or more squarefree factors larger than 1, so Fsf(54)=2.   Let S(n)
    be ∑Fsf(k) for k=2 to n.   S(100)=193.   Find S(10 000 000 000).
    """
    problem_id = 362
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

