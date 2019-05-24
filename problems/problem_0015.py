from pyler import EulerProblem
from math import factorial


class Problem0015(EulerProblem):
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.   How many such routes are there through a 20×20 grid?
    """

    problem_id = 15
    simple_input = 2
    simple_output = 6
    real_input = 20
    real_output = 137846528820

    @staticmethod
    def solver(input_val):
        poids = []

        for i in range(input_val + 1):
            poids.append((input_val + 1) * [1])

        for i in range(input_val + 1):
            for j in range(i + 1):
                if j == 0:
                    poids[i][0] = 1
                elif j - i == 0:
                    poids[0][i] = 1
                else:
                    poids[i - j][j] = poids[i - j - 1][j] + poids[i - j][j - 1]

        for j in range(1, input_val + 1):
            for i in range(input_val, j - 1, -1):
                poids[i][j + input_val - i] = (
                    poids[i - 1][j + input_val - i] + poids[i][j + input_val - i - 1]
                )

        return poids[input_val][input_val]

    @staticmethod
    def solver2(input_val):
        """ Recursive algorithm with memoization """
        cache = dict()

        def count_routes(m, n):
            if n == 0 or m == 0:
                return 1
            if (m, n) in cache:
                return cache[(m, n)]
            cache[(m, n)] = count_routes(m, n - 1) + count_routes(m - 1, n)
            return cache[(m, n)]

        return count_routes(input_val, input_val)

    @staticmethod
    def solver3(input_val):
        """ Iterative solution close to solver """
        grid = [[1] * (input_val + 1)] * (input_val + 1)

        for i in range(1, input_val + 1):
            for j in range(1, input_val + 1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[input_val][input_val]

    @staticmethod
    def solver4(input_val):
        """ Combinatorial solution """
        return factorial(2 * input_val) // factorial(input_val) // factorial(input_val)


if __name__ == "__main__":
    import unittest

    unittest.main()
