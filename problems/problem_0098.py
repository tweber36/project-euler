from pyler import EulerProblem


class Problem0098(EulerProblem):
    """
    By replacing each of the letters in the word CARE with 1, 2, 9, and 6
    respectively, we form a square number: 1296 = 362. What is remarkable is
    that, by using the same digital substitutions, the anagram, RACE, also forms
    a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram
    word pair and specify further that leading zeroes are not permitted, neither
    may a different letter have the same digital value as another letter. Using
    words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, find all the square
    anagram word pairs (a palindromic word is NOT considered to be an anagram of
    itself). What is the largest square number formed by any member of such a
    pair? NOTE: All anagrams formed must be contained in the given text file.
    """
    problem_id = 98
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

