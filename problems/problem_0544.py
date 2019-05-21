from pyler import EulerProblem


class Problem0544(EulerProblem):
    """
    Let F(r,c,n) be the number of ways to colour a rectangular grid with r rows
    and c columns using at most n colours such that no two adjacent cells share
    the same colour. Cells that are diagonal to each other are not considered
    adjacent. For example, F(2,2,3) = 18, F(2,2,20) = 130340, and F(3,4,6) =
    102923670. Let S(r,c,n) = $\sum_{k=1}^{n}$ F(r,c,k). For example, S(4,4,15)
    mod 109+7 = 325951319. Find S(9,10,1112131415) mod 109+7.
    """
    problem_id = 544
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

