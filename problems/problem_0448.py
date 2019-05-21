from pyler import EulerProblem


class Problem0448(EulerProblem):
    """
    The function lcm(a,b) denotes the least common multiple of a and b. Let A(n)
    be the average of the values of lcm(n,i) for 1≤i≤n. E.g: A(2)=(2+2)/2=2 and
    A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32.   Let S(n)=∑A(k) for 1≤k≤n.
    S(100)=122726.   Find S(99999999019) mod 999999017.
    """
    problem_id = 448
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

