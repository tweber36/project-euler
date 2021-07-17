import unittest

from pyler.pyler import EulerProblem


class Problem0017(EulerProblem, unittest.TestCase):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the
    numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?  NOTE: Do not count spaces or hyphens. For
    example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
    hundred and fifteen) contains 20 letters. The use of "and" when writing out
    numbers is in compliance with British usage.
    """

    problem_id = 17
    simple_input = 5
    simple_output = 19
    real_input = 1000
    real_output = 21124

    @staticmethod
    def solver(input_val):
        """ Works for input_val up to 1000 """
        numbers = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            1000: "onethousand",
        }
        for i in range(1, input_val + 1):
            if i not in numbers.keys():
                if i < 100:
                    numbers[i] = numbers[i // 10 * 10] + numbers[i % 10]
                else:
                    numbers[i] = numbers[i // 100] + "hundred"
                    if i % 100:
                        numbers[i] += "and" + numbers[i % 100]

        return sum(len(x) for i, x in numbers.items() if i <= input_val)


if __name__ == "__main__":
    unittest.main()
