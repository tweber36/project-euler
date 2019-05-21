from pyler import EulerProblem


class Problem0615(EulerProblem):
    """
    Consider the natural numbers having at least 5 prime factors, which don't
    have to be distinct. Sorting these numbers by size gives a list which starts
    with:  32=2⋅2⋅2⋅2⋅2 48=2⋅2⋅2⋅2⋅3 64=2⋅2⋅2⋅2⋅2⋅2 72=2⋅2⋅2⋅3⋅3 80=2⋅2⋅2⋅2⋅5
    96=2⋅2⋅2⋅2⋅2⋅3    ... So, for example, the fifth number with at least 5
    prime factors is 80.   Find the millionth number with at least one million
    prime factors.  Give your answer modulo 123454321.
    """
    problem_id = 615
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

