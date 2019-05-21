from pyler import EulerProblem


class Problem0232(EulerProblem):
    """
    Two players share an unbiased coin and take it in turns to play "The Race".
    On Player 1's turn, he tosses the coin once: if it comes up Heads, he scores
    one point; if it comes up Tails, he scores nothing. On Player 2's turn, she
    chooses a positive integer T and tosses the coin T times: if it comes up all
    Heads, she scores 2T-1 points; otherwise, she scores nothing. Player 1 goes
    first. The winner is the first to 100 or more points. On each turn Player 2
    selects the number, T, of coin tosses that maximises the probability of her
    winning. What is the probability that Player 2 wins? Give your answer
    rounded to eight decimal places in the form 0.abcdefgh .
    """
    problem_id = 232
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

