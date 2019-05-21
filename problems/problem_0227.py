from pyler import EulerProblem


class Problem0227(EulerProblem):
    """
    "The Chase" is a game played with two dice and an even number of players.
    The players sit around a table; the game begins with two opposite players
    having one die each. On each turn, the two players with a die roll it. If a
    player rolls a 1, he passes the die to his neighbour on the left; if he
    rolls a 6, he passes the die to his neighbour on the right; otherwise, he
    keeps the die for the next turn. The game ends when one player has both dice
    after they have been rolled and passed; that player has then lost. In a game
    with 100 players, what is the expected number of turns the game lasts? Give
    your answer rounded to ten significant digits.
    """
    problem_id = 227
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

