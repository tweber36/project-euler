from pyler import EulerProblem


class Problem0037(EulerProblem):
    """
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3. Find the sum of the only eleven primes that are
    both truncatable from left to right and right to left. NOTE: 2, 3, 5, and 7
    are not considered to be truncatable primes.
    """
    problem_id = 37
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

