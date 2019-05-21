from pyler import EulerProblem


class Problem0655(EulerProblem):
    """
    The numbers $545$, $5\,995$ and $15\,151$ are the three smallest palindromes
    divisible by $109$. There are nine palindromes less than $100\,000$ which
    are divisible by $109$. How many palindromes less than $10^{32}$ are
    divisible by $10\,000\,019\,$ ?
    """
    problem_id = 655
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

