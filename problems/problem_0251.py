from pyler import EulerProblem


class Problem0251(EulerProblem):
    """
    A triplet of positive integers (a,b,c) is called a Cardano Triplet if it
    satisfies the condition: $$\sqrt[3]{a + b \sqrt{c}} + \sqrt[3]{a - b
    \sqrt{c}} = 1$$   For example, (2,1,5) is a Cardano Triplet.   There exist
    149 Cardano Triplets for which a+b+c ≤ 1000.   Find how many Cardano
    Triplets exist such that a+b+c ≤ 110,000,000.
    """
    problem_id = 251
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

