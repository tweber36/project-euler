from pyler import EulerProblem


class Problem0645(EulerProblem):
    """
    On planet J, a year lasts for $D$ days. Holidays are defined by the two
    following rules. At the beginning of the reign of the current Emperor, his
    birthday is declared a holiday from that year onwards. If both the day
    before and after a day $d$ are holidays, then $d$ also becomes a holiday.
    Initially there are no holidays. Let $E(D)$ be the expected number of
    Emperors to reign before all the days of the year are holidays, assuming
    that their birthdays are independent and uniformly distributed throughout
    the $D$ days of the year. You are given $E(2)=1$, $E(5)=31/6$,
    $E(365)\approx 1174.3501$. Find $E(10000)$. Give your answer rounded to 4
    digits after the decimal point.
    """
    problem_id = 645
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

