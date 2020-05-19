import unittest

from pyler import EulerProblem


class Problem0028(EulerProblem, unittest.TestCase):
    """
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows: 21 22 23 24 25 20  7  8  9 10 19  6  1
     2 11 18  5  4  3 1217 16 15 14 13 It can be verified that the sum of the
    numbers on the diagonals is 101. What is the sum of the numbers on the
    diagonals in a 1001 by 1001 spiral formed in the same way?
    """

    problem_id = 28
    simple_input = 5
    simple_output = 101
    real_input = 1001
    real_output = 669171001

    def solver(self, input_val):
        """ Explicit the corner values of each square of size i """
        if input_val < 2 or input_val % 2 == 0:
            raise ValueError(
                """Impossible de créer la spirale avec une taille inférieure à 2 ou 
                un nombre pair de colonnes"""
            )
        else:
            result = 1
            for i in range(3, input_val + 1, 2):
                result += 4 * i ** 2 - 6 * (i - 1)
            return result

    def solver2(self, input_val):
        """
        Explicit formula for the sum of corner values for each square.
        Useful sums:
        1 + 3 + .. + (2n + 1) = (n+1)²
        1² + 3² + ... + (2n + 1)² = (n+1)/3 * (4(n+1)² - 1)
        """
        if input_val < 2 or input_val % 2 == 0:
            raise ValueError(
                """Impossible de créer la spirale avec une taille inférieure à 2 ou 
                un nombre pair de colonnes"""
            )
        else:
            n = (input_val - 1) // 2
            return 2 / 3 * n * (8 * n ** 2 + 15 * n + 13) + 1


if __name__ == "__main__":
    unittest.main()
