import unittest

from pyler.pyler import EulerProblem


class Problem0067(EulerProblem, unittest.TestCase):
    """
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23. 37 4 2 4 6 8 5
    9 3 That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom
    in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file
    containing a triangle with one-hundred rows. NOTE: This is a much more
    difficult version of Problem 18. It is not possible to try every route to
    solve this problem, as there are 299 altogether! If you could check one
    trillion (1012) routes every second it would take over twenty billion years
    to check them all. There is an efficient algorithm to solve it. ;o)
    """

    problem_id = 67
    simple_input = """3
    7 4
    2 4 6
    8 5 9 3"""
    simple_output = 23
    with open("p067_triangle.txt") as f:
        real_input = f.read()
    real_output = 7273

    @staticmethod
    def solver(input_val):
        """
                The idea is to start from the end.
                At a number on the layer i, you can look at the two numbers possible
                from layer i+1 and choose the highest to add to the number on layer i.
                And so on until you reach the first layer with only one number.
                """
        grid = list(map(lambda x: list(map(int, x.split())), input_val.split("\n")))

        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[i])):
                if grid[i + 1][j] >= grid[i + 1][j + 1]:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += grid[i + 1][j + 1]
        return grid[0][0]


if __name__ == "__main__":
    unittest.main()
