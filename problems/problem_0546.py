from pyler import EulerProblem


class Problem0546(EulerProblem):
    """
    Define fk(n) = $\sum_{i=0}^{n}$ fk($\lfloor\frac{i}{k}\rfloor$) where fk(0)
    = 1 and $\lfloor x \rfloor$ denotes the floor function. For example, f5(10)
    = 18, f7(100) = 1003, and f2(103) = 264830889564. Find $(\sum_{k=2}^{10}$
    fk(1014)$)$ mod (109+7).
    """
    problem_id = 546
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

