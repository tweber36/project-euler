from pyler import EulerProblem


class Problem0641(EulerProblem):
    """
    Consider a row of $n$ dice all showing 1. First turn every second die,$
    (2,4,6,\ldots)$, so that the number showing is increased by 1. Then turn
    every third die. The sixth die will now show a 3. Then turn every fourth die
    and so on until every $n$th die (only the last die) is turned. If the die to
    be turned is showing a 6 then it is changed to show a 1. Let $f(n)$ be the
    number of dice that are showing a 1 when the process finishes. You are given
    $f(100)=2$ and $f(10^8) = 69$. Find $f(10^{36})$.
    """
    problem_id = 641
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

