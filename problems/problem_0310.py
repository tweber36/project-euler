from pyler import EulerProblem


class Problem0310(EulerProblem):
    """
    Alice and Bob play the game Nim Square. Nim Square is just like ordinary
    three-heap normal play Nim, but the players may only remove a square number
    of stones from a heap. The number of stones in the three heaps is
    represented by the ordered triple (a,b,c). If 0≤a≤b≤c≤29 then the number of
    losing positions for the next player is 1160.   Find the number of losing
    positions for the next player if 0≤a≤b≤c≤100 000.
    """
    problem_id = 310
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

