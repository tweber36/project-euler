import unittest
from itertools import count

from pyler.pyler import EulerProblem


class Problem0026(EulerProblem, unittest.TestCase):
    """
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:  1/2= 0.5 1/3= 0.(3)
    1/4= 0.25 1/5= 0.2 1/6= 0.1(6) 1/7= 0.(142857) 1/8= 0.125 1/9= 0.(1)
    1/10= 0.1  Where 0.1(6) means 0.166666..., and has a 1-digit recurring
    cycle. It can be seen that 1/7 has a 6-digit recurring cycle. Find the value
    of d < 1000 for which 1/d contains the longest recurring cycle in its
    decimal fraction part.
    """

    problem_id = 26
    simple_input = 10
    simple_output = 7
    real_input = 1000
    real_output = 983

    @staticmethod
    def solver(input_val):
        def recurring_cycle_length(n):
            if n <= 1:
                raise ValueError("n should be > 2")
            q, r = divmod(10, n)
            div_history = []
            while (q, r) not in div_history:
                div_history.append((q, r))
                q, r = divmod(10 * r, n)
            return len(div_history)

        max_recur_len, number = max(
            (recurring_cycle_length(i), i) for i in range(2, input_val)
        )
        return number

    @staticmethod
    def solver2(input_val):
        def recurring_cycle_length(n):
            remainder = 10  # initial remainder: 10 * (1 % n)
            remainders_seen = {}  # remainders first pos
            for i in count(0):
                if remainder == 0:
                    return 0  # divides evenly
                elif remainder in remainders_seen:
                    return i - remainders_seen[remainder]  # curpos - firstpos
                remainders_seen[remainder] = i
                remainder = 10 * (remainder % n)

        max_recur_len, number = max(
            (recurring_cycle_length(i), i) for i in range(2, input_val)
        )
        return number


if __name__ == "__main__":
    unittest.main()
