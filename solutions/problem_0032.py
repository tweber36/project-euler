from pyler.pyler import EulerProblem


class Problem0032(EulerProblem):
    """
    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
    through 5 pandigital. The product 7254 is unusual, as the identity, 39 × 186
    = 7254, containing multiplicand, multiplier, and product is 1 through 9
    pandigital. Find the sum of all products whose
    multiplicand/multiplier/product identity can be written as a 1 through 9
    pandigital. HINT: Some products can be obtained in more than one way so be
    sure to only include it once in your sum.
    """
    problem_id = 32
    simple_input = 0
    simple_output = 45228
    real_input = 0
    real_output = 45228

    @staticmethod
    def solver(input_val):
        def is_pandigital(i, j):
            n = i * j
            digits = str(i) + str(j) + str(n)
            digits_set = set(digits)
            if '0' in digits:
                return False
            elif len(digits) == 9 and len(digits_set) == 9:
                return True
            else:
                return False

        prods = set()
        for i in range(100):
            for j in range(i, 10000):
                if is_pandigital(i, j):
                    n = i * j
                    prods.add(n)
        return sum(prods)

    @staticmethod
    def solver2(input_val):
        p = set()
        for a in range(1, 100):
            for b in range(1, 9999 // a):
                if ''.join(sorted("%d%d%d" % (a, b, a * b))) == '123456789':
                    p.add(a * b)
        return sum(p)


if __name__ == '__main__':
    import unittest
    unittest.main()

