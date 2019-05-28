import unittest
from pyler import EulerProblem


class Problem0022(EulerProblem, unittest.TestCase):
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score. For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
    list. So, COLIN would obtain a score of 938 × 53 = 49714. What is the total
    of all the name scores in the file?
    """

    problem_id = 22
    simple_input = "p022_names.txt"
    simple_output = 871198282
    real_input = "p022_names.txt"
    real_output = 871198282

    def solver(self, input_val):
        with open(input_val) as f:
            names = f.read().split(",")
            names.sort()
            names = [s.replace('"', "") for s in names]

        def value_name(name):
            return sum(ord(char) - 64 for char in name)

        return sum((idx + 1) * value_name(name) for idx, name in enumerate(names))


if __name__ == "__main__":
    unittest.main()
