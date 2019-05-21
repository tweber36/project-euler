from pyler import EulerProblem


class Problem0543(EulerProblem):
    """
    Define function P(n,k) = 1 if n can be written as the sum of k prime numbers
    (with repetitions allowed), and P(n,k) = 0 otherwise. For example, P(10,2) =
    1 because 10 can be written as either 3 + 7 or 5 + 5, but P(11,2) = 0
    because no two primes can sum to 11. Let S(n) be the sum of all P(i,k) over
    1 ≤ i,k ≤ n. For example, S(10) = 20, S(100) = 2402, and S(1000) = 248838.
    Let F(k) be the kth Fibonacci number (with F(0) = 0 and F(1) = 1). Find the
    sum of all S(F(k)) over 3 ≤ k ≤ 44
    """
    problem_id = 543
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

