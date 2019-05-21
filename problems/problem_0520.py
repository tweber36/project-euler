from pyler import EulerProblem


class Problem0520(EulerProblem):
    """
    We define a simber to be a positive integer in which any odd digit, if
    present, occurs an odd number of times, and any even digit, if present,
    occurs an even number of times. For example, 141221242 is a 9-digit simber
    because it has three 1's, four 2's and two 4's.  Let Q(n) be the count of
    all simbers with at most n digits. You are given Q(7) = 287975 and Q(100)
    mod 1 000 000 123 = 123864868. Find (∑1≤u≤39 Q(2u)) mod 1 000 000 123.
    """
    problem_id = 520
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

