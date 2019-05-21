from pyler import EulerProblem


class Problem0042(EulerProblem):
    """
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
    so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
    ... By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.
    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, how many are triangle
    words?
    """
    problem_id = 42
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

