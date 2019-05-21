from pyler import EulerProblem


class Problem0019(EulerProblem):
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

