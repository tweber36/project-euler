from pyler import EulerProblem


class Problem0081(EulerProblem):
    """
    In the 5 by 5 matrix below, the minimal path sum from the top left to the
    bottom right, by only moving to the right and down, is indicated in bold red
    and is equal to 2427.  $$ \begin{pmatrix} \color{red}{131} & 673 & 234 & 103
    & 18\\ \color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
    630 & 803 & \color{red}{746} & \color{red}{422} & 111\\ 537 & 699 & 497 &
    \color{red}{121} & 956\\ 805 & 732 & 524 & \color{red}{37} &
    \color{red}{331} \end{pmatrix} $$  Find the minimal path sum, in matrix.txt
    (right click and "Save Link/Target As..."), a 31K text file containing a 80
    by 80 matrix, from the top left to the bottom right by only moving right and
    down.
    """
    problem_id = 81
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

