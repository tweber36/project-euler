import unittest

from pyler import EulerProblem


class Problem0019(EulerProblem, unittest.TestCase):
    """
    You are given the following information, but you may prefer to do some
    research for yourself. 1 Jan 1900 was a Monday. Thirty days has September,
    April, June and November. All the rest have thirty-one, Saving February
    alone, Which has twenty-eight, rain or shine. And on leap years, twenty-
    nine. A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400. How many Sundays fell on the first of
    the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """

    problem_id = 19
    simple_input = 1
    simple_output = 171
    real_input = 1
    real_output = 171

    def solver(self, input_val):
        def leap_year(x):
            return 29 if (x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)) else 28

        def number_of_days(x):
            return [31, leap_year(x), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        answer = 0
        last_sunday = 0

        for i in range(1900, 2001):
            for j in number_of_days(i):
                last_sunday += -(j % 7)
                if last_sunday <= -7:
                    last_sunday += 7
                if last_sunday == -6 and i >= 1901:
                    answer += 1

        return answer


if __name__ == "__main__":
    unittest.main()
