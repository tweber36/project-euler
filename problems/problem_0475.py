from pyler import EulerProblem


class Problem0475(EulerProblem):
    """
    12n musicians participate at a music festival. On the first day, they form
    3n quartets and practice all day. It is a disaster. At the end of the day,
    all musicians decide they will never again agree to play with any member of
    their quartet. On the second day, they form 4n trios, each musician avoiding
    his previous quartet partners. Let f(12n) be the number of ways to organize
    the trios amongst the 12n musicians. You are given f(12) = 576 and f(24) mod
    1 000 000 007 = 509089824. Find f(600) mod 1 000 000 007.
    """
    problem_id = 475
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

