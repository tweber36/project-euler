from pyler import EulerProblem


class Problem0383(EulerProblem):
    """
    Let f5(n) be the largest integer x for which 5x divides n. For example,
    f5(625000) = 7.   Let T5(n) be the number of integers i which satisfy
    f5((2·i-1)!) < 2·f5(i!) and 1 ≤ i ≤ n. It can be verified that T5(103) = 68
    and T5(109) = 2408210.   Find T5(1018).
    """
    problem_id = 383
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

